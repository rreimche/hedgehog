 # coding=utf-8
from django.db import models
from django import forms

# Create your models here.

class ContactForm(forms.Form):
	name = forms.CharField(label="Ваше имя", max_length=100)
	email = forms.EmailField(label="Ваш адрес электронной почты")
	message = forms.CharField(label="Сообщение", widget=forms.Textarea)
