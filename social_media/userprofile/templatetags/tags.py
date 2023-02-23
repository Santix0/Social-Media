from django import template

from ..models import *
from community.models import *

register = template.Library()


# checking if searching query find any users or communities
# using in searching system
@register.simple_tag
def check_presence_of_users(users: FollowToUser or User, communites: Community) -> bool:
    return True if users or communites else False


# checking if user follow another user
# using in followers.html
@register.simple_tag
def check_subscription(follower: User, to_who_followed: User):

    follow = FollowToUser.objects.filter(followed_user=follower, to_user=to_who_followed)

    if follow: return True
    else: return False


# check if user has any followers
@register.simple_tag
def check_presence_of_followers(user: dict):
    # Checking if dict is not empty
    return True if user else False


# check if user on his page
@register.simple_tag
def check_if_the_same_user(page_user_id: id, user_id: id):
    return True if page_user_id == user_id else False


@register.simple_tag
def check_presence_of_follows(user: User):
    follow_object = FollowToUser.objects.filter(followed_user=user)

    return True if follow_object else False


@register.simple_tag
def check_presence_of_comments(comments: CommentToUserPost) -> bool:
    return True if comments else False


# checking if the post is user's
@register.simple_tag
def check_if_users_post(post: CommunityPost or UserPost) -> bool:
    return isinstance(post, UserPost)


# checkingif post is of community
@register.simple_tag()
def check_if_community_post(post: CommunityPost) -> bool:
    return isinstance(post, CommunityPost)


# check if any posts on main_page
@register.simple_tag
def check_presence_of_posts(posts: list[CommunityPost or UserPost]) -> bool:
    '''
    checking if on page are any posts
    :param posts: list of post of user or community
    :return: bool
    '''
    return True if posts else False


@register.simple_tag
def get_to_user(users: FollowToUser) -> FollowToUser.to_user:
    for user in users:
        return f'{user.to_user.first_name} {user.to_user.last_name}'
