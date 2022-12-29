from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .utils import *


Gender = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Gay', 'Gay'),
    ('Lesbian', 'Lesbian'),
    ('Bisexual', 'Bisexual'),
]


# Custom user
class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/avatars/photos', blank=True, default='media/default_avatar/default.jpg')
    birthday = models.IntegerField('birthday', blank=True,
                                   help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                                   default=0,
                                   )
    phone_number = models.IntegerField('phone number', default=0, blank=True,
                                       validators=[validation_of_number])
    # short description
    bio = models.CharField('bio', max_length=500, default='Nothing', blank=True)
    gender = models.CharField('gender', choices=Gender, max_length=30, blank=True)
    place_of_work = models.CharField('Work place', max_length=200, default='Undefind', blank=True)
    place_of_study = models.CharField('Study place', max_length=200, default='Undefind', blank=True)
    first_name = models.CharField('first_name', max_length=150)
    last_name = models.CharField('last_name', max_length=150)

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.username


# Photos that related to user, they will displaied on users page
class Photo(models.Model):
    img = models.ImageField(upload_to='media/photos')
    reference_to_user = models.ForeignKey(User, on_delete=models.CASCADE)
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
