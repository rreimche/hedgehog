from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Question(models.Model):
	question = models.CharField(max_length=200)
	answer = RichTextUploadingField(null=True)

	def __str__(self):
		return self.question.encode('utf-8')
