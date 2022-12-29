from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    # list_display = ('username', 'email', 'first_name',
    #                 'last_name', 'password', 'avatar',
    #                 'bio', 'birthday', 'gender',
    #                 'phone_number', 'place_of_work', 'place_of_study',
    #                 'is_staff', 'is_active',
    #                 'date_joined', 'last_login'
    #                 )
    exclude = ('password',)

    class Meta:
        model = User
        # exclude = ['password']


class FollowToUserAdmin(admin.ModelAdmin):
    ...


class PhotoAdmin(admin.ModelAdmin):
    ...


admin.site.register(Photo, PhotoAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(FollowToUser, FollowToUserAdmin)

