from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
#from django.template import RequestContext, loader
from .models import Page
from mailers.models import ContactForm
from django.views import generic

# Create your views here.

#def detail(request, page_id):
#	page = get_object_or_404(Page, id = page_id) 	
#	return render(request, 'pages/page_detail.html', {'page':page})

def home(request):
	contact_form = ContactForm()
	return render(request, 'pages/home.html', {'contact_form' : contact_form})

class DetailView(generic.DetailView):
	model = Page
	#template_name = 'pages/detail.html'