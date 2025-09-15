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

