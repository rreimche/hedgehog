from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	fields=['title', 'content']

admin.site.register(Page, PageAdmin)
