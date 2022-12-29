from django import template

from ..models import *

register = template.Library()


@register.simple_tag
def get_avatar(user_id):
    # get user object by id
    user = User.objects.get(id=user_id)

    # return url to user's avatar
    return user.avatar.url


@register.simple_tag
def check_precense_of_users(users: FollowToUser or User) -> bool:
    return True if users else False
