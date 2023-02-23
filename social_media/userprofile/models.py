from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .utils import *

from phonenumber_field.modelfields import PhoneNumberField
from birthday import BirthdayField


# Choices for gender of user (line 40)
Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Gay', 'Gay'),
    ('Lesbian', 'Lesbian'),
    ('Bisexual', 'Bisexual'),
]

# Choices for relation (line 46)
RELATIONSHIP_STATUS = [
    ('Single', 'Single'),
    ('In love', 'In love'),
    ('In relationship', 'In relationship'),
    ('Married', 'Married'),
    ('Engaged', 'Engaged'),
    ('Actively searching', 'Actively searching'),
]


# Custom user
class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars/photos', blank=True, default='media/default_avatar/default.jpg')
    birthday_of_user = BirthdayField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    # short description
    bio = models.CharField('bio', max_length=500, default='Nothing', blank=True)
    # gender is with choices(choices on line 12)
    gender = models.CharField('gender', choices=Gender, max_length=30, blank=True)
    place_of_work = models.CharField('Work place', max_length=200, default='Undefind', blank=True)
    place_of_study = models.CharField('Study place', max_length=200, default='Undefind', blank=True)
    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)
    hobbies = models.CharField('Hobbies', max_length=200, blank=True, null=True)
    # relationship status is with choices(choices on line 20)
    relationship = models.CharField('Relationship', max_length=50, choices=RELATIONSHIP_STATUS, blank=True, null=True)
    political_view = models.CharField('Political views', max_length=100, blank=True, null=True)
    religion = models.CharField('Religion', max_length=100, blank=True, null=True)
    favorite_music = models.CharField('Favorite music', max_length=100, blank=True, null=True)
    favorite_movies = models.CharField('Favorite movies', max_length=100, blank=True, null=True)
    favorite_books = models.CharField('Favorite books', max_length=100, blank=True, null=True)
    town_of_living = models.CharField('Town of living', max_length=150, blank=True, null=True)
    posts = models.ManyToManyField('UserPost')

    class Meta:
        db_table = 'auth_user'
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('gender', 'username', 'first_name',
                     'last_name',
                   )
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserPost(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/photos')
    description = models.CharField(max_length=200, blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('writer',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class FollowToUser(models.Model):
    # User that get follow
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    # User that are following
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return f'{self.to_user.first_name} {self.to_user.last_name}'

    def avatar(self, followed_user):
        user = User.objects.get(id=followed_user)

        return user.avatar.url

    class Meta:
        ordering = ('to_user', 'followed_user',)
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'


class CommentToUserPost(models.Model):
    # user that wrote comment
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField('Comment', max_length=100)
    # post that user comment
    commented_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('posted', 'commented_post', 'commentator',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
