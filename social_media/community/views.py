from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView

from .models import *
from .forms import *


def main_page_of_community(request, community_id: int):
    # get community by id
    community = Community.objects.get(id=community_id)

    # get posts of community
    posts = CommunityPost.objects.filter(writer=community_id).order_by('-posted').select_related('writer',)

    context = {
        'community': community,
        'posts': posts,
    }

    return render(request, 'community/main_page_of_community.html', context)


def communities_of_user(request, user_id: int):
    # get all communities of user
    communities = Followers.objects.filter(follower=user_id).select_related('followed_community',)

    context = {
        'communities': communities,
    }

    return render(request, 'community/users_communities.html', context)


def follow_community(request, community_id: int, role: Followers.role = None):
    # get community to which follow
    community = Community.objects.get(id=community_id)

    # checking what role was gave, None==Participant, else put role that is given
    if role is None:
        role = 'Participant'

    # create Followers object
    Followers.objects.create(follower=request.user, followed_community=community, role=role)

    return HttpResponseRedirect(reverse('main_page_of_community', args=(f'{community_id}')))


def unfollow_community(request, community_id: int):
    # get Followers object by community_id and user id and delete it
    Followers.objects.get(follower=request.user.id, followed_community=community_id).delete()

    return HttpResponseRedirect(reverse('main_page_of_community', args=(f'{community_id}')))


def create_community(request):
    if request.method == 'POST':
        form = CreateCommunityForm(request.POST, request.FILES)

        if form.is_valid():
            # saving the form in attr, because it needs to add community reference
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            follow_community(request, instance.id, role='Owner')

            return HttpResponseRedirect(reverse('main_page_of_community', args=(f'{instance.id}')))
    else:
        form = CreateCommunityForm()

    context = {
        'form': form
    }

    return render(request, 'community/add_community.html', context)


# redirect to settings that connect with communities
def community_in_settings(request):
    return render(request, 'community/community_in_settings.html')


# show all communities where user is owner
def get_communities_user_is_owner(request):
    # get follow object/s where user is owner
    communities = Followers.objects.filter(follower=request.user, role='Owner').select_related('followed_community')

    context = {
        'communities': communities,
    }

    return render(request, 'community/owner_communities.html', context)


class ChangeCommunityInfo(UpdateView):
    model = Community
    form_class = ChangeCommunityInfoForm
    template_name = 'community/change_community_info.html'
    success_url = 'main_page'


# support function that redirect from ChangeCommunityInfoForm to main_page
def redirect_to_main_page(request):
    return redirect('main_page')


# add post
def add_post_to_community(request, community_id: int):
    '''
    Add post to community
    In template will be tag that check if user has access to this
    :param request:
    :param community_id:
    :return:
    '''
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        community = Community.objects.get(id=community_id)

        if form.is_valid():
            # save form in instance object, because it needs to add community object in it
            instance = form.save(commit=False)
            instance.writer = Community.objects.get(id=community_id)
            instance.save()

            # add manytomany field to community posts
            community.posts.add(instance)

            return HttpResponseRedirect(reverse('main_page_of_community', args=(f'{instance.writer.id}')))

    else:
        form = AddPostForm()

    context = {
        'form': form
    }

    return render(request, 'community/add_post_to_community.html', context)


# show all followers of community
def get_all_followers(request, community_id: int):
    # get community which followers wanna see
    community = Community.objects.get(id=community_id)
    # get Followers object by community, to get all followers
    follow_object = Followers.objects.filter(followed_community=community).select_related('follower')

    # follow_object.follower (like this we call it in template)
    context = {
        'follow_object': follow_object,
        'community': community,
    }

    return render(request, 'community/followers.html', context)


def delete_post_of_community(request, post_id: int, community_id: int):
    """
    Delete post of the community
    In template will be tag that check if user has access to this
    :param request:
    :param post_id:
    :return:
    """
    # get post by id and delete
    post = CommunityPost.objects.get(id=post_id)
    post.delete()
    community = Community.objects.get(id=community_id)
    community.posts.remove(post)

    return HttpResponseRedirect(reverse('main_page_of_community', args=(f'{post.writer.id}')))


class EditPost(UpdateView):
    '''
    Edit post of the community
    In template will be tag that checking if user has access for that
    '''
    model = CommunityPost
    form_class = EditPostForm
    template_name = 'community/edit_post.html'
    success_url = 'main_page'


def delete_comment(request, comment_id: int):
    # get comment by id and delete
    comment = CommentsToCommunityPosts.objects.get(id=comment_id)
    CommentsToCommunityPosts.objects.get(id=comment_id).delete()

    # redirect to comment section of current post
    return HttpResponseRedirect(reverse('community_comment_section', args=(f'{comment.commented_post.id}',)))


class EditComment(UpdateView):
    model = CommentsToCommunityPosts
    form_class = EditCommentForm
    success_url = 'main_page'
    template_name = 'community/edit_comment.html'


# show all comments under communiy post and user able to add comment
def community_comment_section(request, post_id: int):
    '''
    # First part
    Show all comments under community's post
    # Second part
    Allow user to add comment
    :param request:
    :param post_id:
    :return:
    '''
    # First part
    # get comments under post
    comments = CommentsToCommunityPosts.objects.filter(commented_post=post_id).order_by('-posted').select_related('commentator', 'commented_post',)
    post = CommunityPost.objects.get(id=post_id)

    # Second part
    if request.method == 'POST':
        form = AddCommentToPostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.commentator, instance.commented_post = request.user, post
            instance.save()

            # redirect to comment section of current post
            return HttpResponseRedirect(reverse('community_comment_section', args=(f'{post_id}',)))

    else:
        form = AddCommentToPostForm()

    context = {
        'comments': comments,
        'form': form,
    }

    return render(request, 'community/community_comments_section.html', context)


