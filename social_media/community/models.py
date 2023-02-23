from django.db import models

from userprofile.models import *

ROLES = [
    ('Participant', 'Participant'),  # can just view post
    ('Worker', 'Worker'),  # can post, delete, change posts
    ('Owner', 'Owner'),  # owner of community, can do all
]

THEMES = [
    ('Undefind', 'Undefind'),
    ('Music', 'Music'),
    ('Sport', 'Sport'),
    ('Games', 'Games'),
    ('Social', 'Social'),
    ('Politic', 'Politic'),
    ('Culture', 'Culture'),
    ('Education', 'Education'),
]


class Community(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=150)
    bio = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.ImageField(upload_to='media/community_avatars')
    theme = models.CharField(max_length=50, choices=THEMES, blank=True, default='Undefind')
    sub_theme = models.CharField(max_length=50, blank=True, default='Undefind')
    posts = models.ManyToManyField('CommunityPost')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('theme', 'name',)
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'


# class Post(models.Model):
#     community = models.ForeignKey(Community, on_delete=models.CASCADE)
#     photo = models.ImageField(upload_to='media/community_posts_photo')
#     description = models.CharField(max_length=150, blank=True, null=True)
#     date_posted = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ('community',)
#         verbose_name = 'Post'
#         verbose_name_plural = 'Posts'


class CommunityPost(models.Model):
    writer = models.ForeignKey(Community, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/community_posts_photo')
    description = models.CharField(max_length=200, blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('writer',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Followers(models.Model):
    # who follow community
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    # role of follower
    role = models.CharField(max_length=50, choices=ROLES, default='Participant', blank=True)
    # community that is followed
    followed_community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class Meta:
        ordering = ('follower', 'followed_community')
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'


class CommentsToCommunityPosts(models.Model):
    # user that write comment
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField('Comment', max_length=100)
    # post that was commented
    commented_post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('commentator', 'commented_post',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
