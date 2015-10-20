from django.shortcuts import render
from django.views import generic
from .models import Post

class DetailView(generic.DetailView):
	model = Post
	pass

class ListView(generic.ListView):
	model = Post
	pass


