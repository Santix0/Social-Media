from django.contrib import admin

from .models import *


class CommunityAdmin(admin.ModelAdmin):
    ...


class PostAdmin(admin.ModelAdmin):
    ...


class FollowersAdmin(admin.ModelAdmin):
    ...


admin.site.register(Community, CommunityAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Followers, FollowersAdmin)
