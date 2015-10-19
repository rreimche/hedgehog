from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ContactForm

def sendmessage(request): 
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ConcatForm()

    return render(request, 'mailers/contact.html', {'form': form})