from django import template

from ..models import *

register = template.Library()


# check if user follow any communities
@register.simple_tag
def check_precense_of_communities(communities: Community) -> bool:
    return True if communities else False


# checking if user follow community
@register.simple_tag
def check_subscription(follower, to_who_follow):
    follow = Followers.objects.filter(follower=follower, followed_community=to_who_follow)

    if follow:
        return True
    else:
        return False


@register.simple_tag
def check_role(user: User, community: Community) -> bool:
    # checking role
    try:
        # checking if user is owner of this community
        owner_object = Community.objects.get(id=community, owner=user)
        if owner_object:
            return True
        # checking if user is worker or owner of this community
        follow_object = Followers.objects.get(follower=user, followed_community=community)
        if follow_object.role == 'Owner' or follow_object.role == 'Worker':
            return True
    except (Exception,):
        return False


@register.simple_tag
def check_presence_of_comments(comments: CommentsToCommunityPosts) -> bool:
    return True if comments else False


@register.simple_tag
def check_if_users_comment(user_id: id,
                           commentator_id):  # user_id is id of user that on site at moment,
                                            # commentator id is id of user that left comment
    return True if user_id == commentator_id else False
