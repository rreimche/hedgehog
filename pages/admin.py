from django.contrib import admin
from .models import Page

# Register your models here.

#class PageAdminForm(forms.ModelForm):
#	content = forms.CharField(widget=CKEditorWidget())
#	class Meta:
#		model = Page

#class PageAdmin(admin.ModelAdmin):
#	fields=['title', 'content']
#	form = PageAdminForm

admin.site.register(Page)
