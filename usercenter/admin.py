from django.contrib import admin

# Register your models here.
from models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("owner", "avatar")
    list_filter = ("owner",)
    search_filter = ("avatar",)

admin.site.register(UserProfile, UserProfileAdmin)
