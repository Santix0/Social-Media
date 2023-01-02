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
    path('add_post/<int:user_id>', add_post, name='add_post'),
    path('delete_post/<int:post_id>', delete_post, name='delete_post'),
    path('user_follow/<int:user_id>', user_follow, name='user_follow'),
    path('edit_post/<int:pk>', ChangePost.as_view(), name='edit_post'),
    path('edit_post/main_page', redirect_to_main_page, name='redirect_to_main_page_from_edit_post'),
    path('add_comment/<int:user_id>/<int:post_id>', add_comment_to_post, name='add_comment_to_post'),
    path('view_posts_comments/<int:post_id>', show_comments_of_post, name='view_posts_comments'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment_from_user_post'),
    path('edit_comment/<int:pk>', EditComment.as_view(), name='edit_comment_from_user_post'),
    path('edit_comment/main_page', redirect_to_main_page, name='redirect_to_main_page_from_edit_commet'),
]
