from django.urls import path

from .views import *


urlpatterns = [
    path('main_page/<int:community_id>', main_page_of_community, name='main_page_of_community'),
    path('user_communities/<int:user_id>', communities_of_user, name='communities_of_user'),
    path('follow_community/<int:community_id>', follow_community, name='follow_community'),
    path('unfollow_community/<int:community_id>', unfollow_community, name='unfollow_community'),
    path('community_settings/', community_in_settings, name='community_in_settings'),
    path('create_community/', create_community, name='create_community'),
    # path to communities where user is owner
    path('user_is_owner/', get_communities_user_is_owner, name='user_is_owner'),
    path('change_community_info/<int:pk>', ChangeCommunityInfo.as_view(), name='change_community_info'),
    path('change_community_info/main_page/', redirect_to_main_page, name='redirect_to_main_page'),
    path('add_post/<int:community_id>', add_post_to_community, name='add_post_to_community'),
    path('followers/<int:community_id>', get_all_followers, name='all_followers'),
    path('delete_post_of_community/<int:post_id>/<int:community_id>', delete_post_of_community, name='delete_post_of_community'),
    path('edit_post_of_community/<int:pk>', EditPost.as_view(), name='edit_post_of_community'),
    path('edit_post_of_community/main_page', redirect_to_main_page, name='redirect_to_main_page_from_edit'),
    path('delete_comment/<int:comment_id>', delete_comment, name='delete_comment_from_community_post'),
    path('edit_comment/<int:pk>', EditComment.as_view(), name='edit_comment_from_community_post'),
    path('edit_comment/main_page', redirect_to_main_page, name='redirect_to_main_page_from_eidt_comment_community'),
    path('community_comments_section/<int:post_id>', community_comment_section, name='community_comment_section'),
]
