from django import template

from ..models import *
from community.models import Community

register = template.Library()


@register.simple_tag
def get_avatar(user_id):
    # get user object by id
    user = User.objects.get(id=user_id)

    # return url to user's avatar
    return user.avatar.url


# checking if searching query find any users or communities
# using in searching system
@register.simple_tag
def check_precense_of_users(users: FollowToUser or User, communites: Community) -> bool:
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
def check_precense_of_followers(user_id: id):
    # get followers of the user
    followers = FollowToUser.objects.filter(to_user=user_id)

    if followers: return True
    else: return False


# check if user on his page
@register.simple_tag
def check_if_the_same_user(page_user_id: id, user_id: id):
    return True if page_user_id == user_id else False


@register.simple_tag
def check_precense_of_follows(user: User):
    follow_object = FollowToUser.objects.filter(followed_user=user)

    return True if follow_object else False

