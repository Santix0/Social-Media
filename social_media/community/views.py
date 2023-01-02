from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import *
from .forms import *


def main_page_of_community(request, community_id):

    # get community by id
    community = Community.objects.get(id=community_id)

    # get posts of community
    posts = Post.objects.filter(community=community_id)

    context = {
        'community': community,
        'posts': posts,
    }

    return render(request, 'community/main_page_of_community.html', context)


def communities_of_user(request, user_id):
    # get all communities of user
    communities = Followers.objects.filter(follower=user_id)

    context = {
        'communities': communities,
    }

    return render(request, 'community/users_communities.html', context)


def follow_community(request, community_id, role=None):
    # get community to which follow
    community = Community.objects.get(id=community_id)

    # checking what role was gave, None==Participant, else put role that is given
    if role is None:
        role = 'Participant'

    # create Followers object
    Followers.objects.create(follower=request.user, followed_community=community, role=role)

    return redirect('main_page')


def unfollow_community(request, community_id):
    # get Followers object by community_id and user id and delete it
    follow_object = Followers.objects.get(follower=request.user.id, followed_community=community_id).delete()

    return redirect('main_page')


def create_community(request):
    if request.method == 'POST':
        form = CreateCommunityForm(request.POST, request.FILES)

        if form.is_valid():
            # saving the form in attr, because it needs to add community reference
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            follow_community(request, instance.id, role='Owner')

            return redirect('main_page')
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
    follow_object = Followers.objects.filter(follower=request.user, role='Owner')

    communities = follow_object

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
def add_post_to_community(request, community_id):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)

        if form.is_valid():
            # save form in instance object, because it needs to add community object in it
            instance = form.save(commit=False)
            instance.community = Community.objects.get(id=community_id)
            instance.save()

            return redirect('main_page')

    else:
        form = AddPostForm()

    context = {
        'form': form
    }

    return render(request, 'community/add_post_to_community.html', context)


# show all followers of community
def get_all_followers(request, community_id):
    # get community which followers wanna see
    community = Community.objects.get(id=community_id)
    # get Followers object by community, to get all followers
    follow_object = Followers.objects.filter(followed_community=community)

    # follow_object.follower (like this we call it in template)
    context = {
        'follow_object': follow_object,
        'community': community,
    }

    return render(request, 'community/followers.html', context)


def delete_post_of_community(request, post_id: id):
    # get post by id and delete
    Post.objects.get(id=post_id).delete()

    return redirect('main_page')


class EditPost(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'community/edit_post.html'
    success_url = 'main_page'


def add_comment(request, user_id: id, post_id: id):
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        form = AddCommentToPostForm(request.POST)

        if form.is_valid():
            # saving form with commit=false in instance, because we need add commentator and post ids
            instance = form.save(commit=False)
            instance.commentator, instance.commented_post = user, post
            instance.save()
            return redirect('main_page')

    else:
        form = AddCommentToPostForm()

    context = {
        'form': form,
    }

    return render(request, 'community/add_comment_to_post.html', context)


def show_all_comments_of_post(request, post_id: id):
    # get all comments of the post, by post_id
    comments = CommentsToCommunityPosts.objects.filter(commented_post=post_id)

    context = {
        'comments': comments,
    }

    return render(request, 'community/posts_comments.html', context)


def delete_comment(request, comment_id: id):
    # get comment by id and delete
    CommentsToCommunityPosts.objects.get(id=comment_id).delete()

    return redirect('main_page')


class EditComment(UpdateView):
    model = CommentsToCommunityPosts
    form_class = EditCommentForm
    success_url = 'main_page'
    template_name = 'community/edit_comment.html'

