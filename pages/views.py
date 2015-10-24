# coding=utf-8

from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from .models import Page
from faq.models import Question
from mailers.models import ContactForm
from django.views import generic

# Create your views here.

#def detail(request, page_id):
#	page = get_object_or_404(Page, id = page_id) 	
#	return render(request, 'pages/page_detail.html', {'page':page})

class DetailView(generic.DetailView):
	model = Page
	#template_name = 'pages/detail.html'

def home(request):
	context = {
		'contact_form' : ContactForm(),
		'faq_objects' : Question.objects.all()[:8],
	}
	return render(request, 'pages/home.html', context)

def studio(request):
	return render_by_title(request, 'О студии')

def training(request):
	return render_by_title(request, 'Занятия')

def contacts(request):
	return render_by_title(request, 'Контакты')



def render_by_title(request, the_title):
	context = {
		'page' : get_object_or_404(Page, title=the_title),  # TODO page title
	}
	if the_title == 'Контакты':
		context['contact_form'] = ContactForm()
	return render(request, 'pages/page_detail.html', context)
