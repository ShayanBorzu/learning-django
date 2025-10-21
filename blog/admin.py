from django.contrib import admin
from blog.models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created"
    empty_value_display = "-empty-"
    list_display = ("id","title", "status", "created", "published")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    summernote_fields = ('content',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    list_display = ("id","subject", "name", "email")
    list_filter = ("approved",)
    search_fields = ["email", "message"]