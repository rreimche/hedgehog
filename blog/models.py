from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name.encode('utf-8')

class Post(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	content = models.TextField(null=True)
	categories = models.ManyToManyField(Category, blank=True)

	def __str__(self):
		return self.title.encode('utf-8')
