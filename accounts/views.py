from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket submitted successfully.')
        else:
            messages.error(request, 'Ticket didnt submit.')
    form = ContactForm()
    return render(request, 'blog/contact.html')
