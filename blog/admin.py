from django.contrib import admin
from blog.models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    empty_value_display = "-empty-"
    list_display = ("id","title", "status", "created", "published")
    list_filter = ("status",)
    search_fields = ["title", "content"]
