from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .utils import *

from phonenumber_field.modelfields import PhoneNumberField


Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Gay', 'Gay'),
    ('Lesbian', 'Lesbian'),
    ('Bisexual', 'Bisexual'),
]

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
    birthday = models.IntegerField('birthday', blank=True,
                                   help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                                   default=0,
                                   )
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

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username


# Photos that related to user, they will displaied on users page
class Photo(models.Model):
    img = models.ImageField(upload_to='media/photos')
    reference_to_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    posted = models.DateTimeField(auto_now_add=True)


class FollowToUser(models.Model):
    # User that get follow
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    # User that are following
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return f'{self.followed_user.first_name} {self.followed_user.last_name}'

    def avatar(self, followed_user):
        user = User.objects.get(id=followed_user)

        return user.avatar.url


class CommentToUserPost(models.Model):
    # user that wrote comment
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField('Comment', max_length=100)
    # post that user comment
    commented_post = models.ForeignKey(Photo, on_delete=models.CASCADE)
