from django.contrib import admin
from websiteApp.models import *


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass