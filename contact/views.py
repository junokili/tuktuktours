from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import MessageForm
from profiles.models import UserProfile

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

    try:
        profile = UserProfile.objects.get(user=request.user)
        message_form = MessageForm(initial={
            'message_email': profile.default_email,
                })
    except UserProfile.DoesNotExist:
        message_form = MessageForm()

    template = 'contact/contact.html'
    context = {
        'message_form': message_form,
    }

    return render(request, template, context)
