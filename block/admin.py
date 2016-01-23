from django.contrib import admin


# Register your models here.
from models import Block


class BlockAdmin(admin.ModelAdmin):
    list_display = ("namechar", "descriptionchar", "admin", "create_timestamp",
            "last_update_timestamp")
    list_filter = ("namechar",)

admin.site.register(Block, BlockAdmin)
