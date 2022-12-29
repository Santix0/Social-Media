# urls that connected to user
from django.urls import path
from .views import *


urlpatterns = [
    path('<int:user_id>/', user_main_page, name='user_main_page'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', user_logout, name='user_logout'),
    path('change_userprofile/', ChangeUserProfile.as_view(), name='change_userprofile'),
    path('change_userprofile/main_page', redirect_to_main_page, name='redirect_to_main_page'),
    path('full_user_information/<int:user_id>', all_users_information, name='all_users_information'),
    path('user/settings/', user_settings, name='user_settings'),
    path('searcing_users/', searching_users, name='searching_users'),
    path('follow_to_user/<int:to_user_id>/', follow_to_user, name='follow_to_user'),
    path('unfollow_from_user/<int:from_user>/', unfollow_from_user, name='unfollow_from_user'),
    path('all_followers/<int:user_id>', get_all_followers, name='get_all_followers'),
]
