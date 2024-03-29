from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Page(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	#content = models.TextField(null=True)
	content = RichTextUploadingField(null=True)

	def __str__(self):
		return self.title.encode('utf-8')