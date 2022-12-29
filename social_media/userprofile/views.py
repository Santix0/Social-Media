from django.contrib.auth import logout, authenticate, login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .models import *
from .forms import *


# return user info and photos that releted with him
def user_main_page(request, user_id):
    # get user info from db by user's id
    user = User.objects.get(id=user_id)
    # get photos that user have posted
    photos = Photo.objects.filter(reference_to_user_id=user_id)

    context = {
        'user': user,
        'photos': photos,
    }

    return render(request, 'userprofile/user_main_page.html', context)


# return info about user
def all_users_information(request, user_id):
    # get user from db by id
    user = User.objects.get(id=user_id)

    context = {
        'user': user,
    }

    return render(request, 'userprofile/full_users_information.html', context)


def main_page(request):

    return render(request, 'userprofile/main.html')


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

    if not query:
        users = None

    context = {
        'users': users,
    }

    return render(request, 'userprofile/searching_users.html', context)


def follow_to_user(request, to_user_id):
    # get user that get follow
    user = User.objects.get(id=to_user_id)

    # user that are following
    followed_user = User.objects.get(id=request.user.id)

    # create follow object
    FollowToUser.objects.create(to_user=user, followed_user=followed_user)

    return redirect('main_page')


def unfollow_from_user(request, from_user):
    # get user from who will be unfollowed
    user = User.objects.get(id=from_user)

    # user that are unfollowing
    unfollowing_user = User.objects.get(id=request.user.id)

    # delete follower
    FollowToUser.objects.get(to_user=user, followed_user=unfollowing_user).delete()

    return redirect('main_page')


def get_all_followers(request, user_id):
    # get all followers of user
    followers = FollowToUser.objects.filter(to_user=user_id)

    context = {
        'followers': followers,
    }

    return render(request, 'userprofile/followers.html', context)
