# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ContactForm
from django.core.mail import send_mail

def sendmessage(request): 
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			try:
 				message = "Отправитель: {0}\nEmail: {1}\nСообщение: {2}".format(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
				send_mail('Сообщение с Ежесайта', message, 'robot@example.com', ['to@example.com'], fail_silently=False)
			except:
				form.errors['__all__'] = form.error_class(['Что-то пошло не так'])
				return render(request, 'mailers/contact.html', {'contact_form': form})
			else:
				return HttpResponseRedirect('/spasibo/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()

	return render(request, 'mailers/contact.html', {'contact_form': form})

def thankyou(request):
	return render(request, 'mailers/thankyou.html', {})