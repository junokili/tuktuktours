from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import MessageForm

# Create your views here.


def contact(request):

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            messages.success(request, 'Message sent.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to send message. '
                           'Please ensure the form is valid.')
    else:
        message_form = MessageForm()

    template = 'contact/contact.html'
    context = {
        'message_form': message_form,
    }

    return render(request, template, context)
