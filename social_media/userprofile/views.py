from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.core.mail import message
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from community.models import *


# return user info and posts that releted with him
def user_main_page(request, user_id: int):
    # if it's request.user's page we put in user object request.user
    if request.user.id == user_id:
        user = request.user
    else:
        # get user info from db by user's id
        user = User.objects.get(id=user_id)
    # get posts that user had posted
    posts = UserPost.objects.filter(writer=user_id).order_by('-posted').select_related('writer',)
    # check if request.user subscribe the user
    subscription = False
    if FollowToUser.objects.filter(followed_user=request.user, to_user=user):
        subscription = True
    context = {
        'user': user,
        'posts': posts,
        'subscription': subscription,
    }

    return render(request, 'userprofile/user_main_page.html', context)


# return info about user
def all_users_information(request, user_id: int):
    # get user from db by id
    user = User.objects.get(id=user_id)

    context = {
        'user': user,
    }

    return render(request, 'userprofile/full_users_information.html', context)


# return all post of users and communities that user follows
def main_page(request):
    posts_list = []
    users = FollowToUser.objects.filter(followed_user=request.user.id).select_related('to_user')
    communities = Followers.objects.filter(follower=request.user.id).select_related('followed_community')

    for user in users:
        posts_list.append(UserPost.objects.filter(writer=user.id).select_related('writer'))

    for community in communities:
        posts_list.append(CommunityPost.objects.filter(writer=community.id).select_related('writer'))

    context = {
        'posts_list': posts_list,
    }

    return render(request, 'userprofile/main.html', context)


def sign_in(request):
    # checking if method of request is Post
    if request.method == 'POST':
        # getting the username and password of user from form
        username = request.POST.get('username')
        password = request.POST.get('password1')

        # trying to authenticate user
        user = authenticate(request, username=username, password=password)
        form = SignInForm(request.POST)

        # if authentication of user is success and user exists login him
        if user:
            login(request, user)
            return redirect('main_page')
        else:
            ...

    else:
        form = SignInForm()

    context = {
        'form': form
    }

    return render(request, 'userprofile/sign_in.html', context)


def sign_up(request):
    # checking if method of request is Post
    if request.method == 'POST':

        # taking information from form
        form = SignUpForm(request.POST)
        # if form is valid create user
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }

    return render(request, 'userprofile/sign_up.html', context)


def user_logout(request):
    logout(request)
    return redirect('main_page')


# class that change users data
class ChangeUserProfile(UpdateView):
    form_class = ChangeUserProfileForm
    template_name = 'userprofile/change_userprofile.html'
    success_url = 'main_page'

    def get_object(self, *kwargs):
        return self.request.user


# support function that redirect to main page after user change his/her profile info
def redirect_to_main_page(request):
    return redirect('main_page')


# redirect to settings of profile
def user_settings(request):
    return render(request, 'userprofile/profile_settings.html')


# Search the users by first_name, last_name or username
def searching_users(request):
    # get query by user's request in search field
    query = request.GET.get('search', '')

    # filter user by first_name, last_name, username
    users = User.objects.filter(
        Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(username__icontains=query)
    )

    communities = Community.objects.filter(
        Q(name__icontains=query)
    )

    if not query:
        users = None

    context = {
        'users': users,
        'communities': communities,
    }

    return render(request, 'userprofile/searching_users.html', context)


def follow_to_user(request, to_user_id: int):
    # get user that get follow
    user = User.objects.get(id=to_user_id)

    # user that are following
    followed_user = User.objects.get(id=request.user.id)

    # create follow object
    FollowToUser.objects.create(to_user=user, followed_user=followed_user)

    return HttpResponseRedirect(reverse('user_main_page', args=(f'{user.id}')))


def unfollow_from_user(request, from_user: int):
    # get user from who will be unfollowed
    user = User.objects.get(id=from_user)

    # user that are unfollowing
    unfollowing_user = User.objects.get(id=request.user.id)

    # delete follower
    FollowToUser.objects.get(to_user=user, followed_user=unfollowing_user).delete()

    return HttpResponseRedirect(reverse('user_main_page', args=(f'{user.id}')))


# get all users that follow request.user
def get_all_followers(request, user_id: int):
    # get all followers of user
    followers = FollowToUser.objects.filter(to_user=user_id).select_related('to_user', 'followed_user',)

    context = {
        'followers': followers,
    }

    return render(request, 'userprofile/followers.html', context)


# add post
def add_post(request, user_id: int):
    # checking if form method is post
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        # get posts's writer
        user = User.objects.get(id=user_id)
        # check if form fields are valid
        if form.is_valid():
            # save form with commit false, because we gotta add reference_to_user
            instance = form.save(commit=False)
            # to instance add reference_to_user field as User object
            instance.writer = request.user
            instance.save()

            user.posts.add(instance)

            return HttpResponseRedirect(reverse('user_main_page', args=(f'{user_id}')))

    else:
        form = AddPostForm()

    context = {
        'form': form
    }

    return render(request, 'userprofile/add_post.html', context)


# delete post
def delete_post(request, post_id: int):
    # get UserPost object by id and delete
    UserPost.objects.get(id=post_id).delete()
    user = User.objects.get(id=request.user.id)
    user.posts.remove(post_id)

    return HttpResponseRedirect(reverse('user_main_page', args=(f'{request.user.id}')))


# get all users that follow user
def user_follow(request, user_id: int):
    # get follow object where user is follow
    follows = FollowToUser.objects.filter(followed_user=user_id).select_related('followed_user', 'to_user')

    context = {
        'follows': follows,
    }

    return render(request, 'userprofile/user_follow.html', context)


class ChangePost(UpdateView):
    model = UserPost
    form_class = ChangePostForm
    template_name = 'userprofile/change_post.html'
    success_url = 'main_page'


def delete_comment(request, comment_id: int):
    # get comment by id and delete
    comment = CommentToUserPost.objects.get(id=comment_id)
    CommentToUserPost.objects.get(id=comment_id).delete()

    # redirect to comment section of current post
    return HttpResponseRedirect(reverse('comments_section', args=(f'{comment.commented_post.id}',)))


class EditComment(UpdateView):
    model = CommentToUserPost
    form_class = EditCommentForm
    # success_url = HttpResponseRedirect(reverse('comments_section', args=()))
    success_url = 'main_page'
    template_name = 'userprofile/edit_comment.html'


# show all comments under post and user able to add comment
# function cannot be divided into two, because they have reference to one html file
def comments_under_post(request, post_id: int):
    # First part of function
    # get all comments related to post
    # get them by id of post
    comments = CommentToUserPost.objects.filter(commented_post=post_id).order_by('-posted').select_related('commentator')

    # Second part of function
    # add comment to user post
    post = UserPost.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentToUserPostForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            # set commentator id and what post was commented
            instance.commentator, instance.commented_post = request.user, post
            instance.save()

            # redirect to comment section of current post
            return HttpResponseRedirect(reverse('comments_section', args=(post_id,)))

    else:
        form = CommentToUserPostForm()

    # in context will be form and comments that already add to this post
    context = {
        'comments': comments,
        'form': form,
    }

    return render(request, 'userprofile/comments_section.html', context)
