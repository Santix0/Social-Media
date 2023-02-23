from django.contrib import admin

from .models import *


class CommunityAdmin(admin.ModelAdmin):
    ...


class CommunityPostAdmin(admin.ModelAdmin):
    ...


class FollowersAdmin(admin.ModelAdmin):
    ...


admin.site.register(Community, CommunityAdmin)
admin.site.register(CommunityPost, CommunityPostAdmin)
admin.site.register(Followers, FollowersAdmin)
