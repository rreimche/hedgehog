#from django.shortcuts import render  #, get_object_or_404
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from .models import Question
from django.views import generic

class DetailView(generic.DetailView):
	model = Question

class ListView(generic.ListView):
	model = Question