from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
# Create your views here.


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your shopping basket is currently empty")
        return redirect(reverse('tours'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ht9HFLpEsCk7L28N5hR3qGSv0j2IUoaYHD3hd6ZQb2Rg2SylJNJMFqsoEoyayMhHmrysr1IzV9XO2iFjcwSWhMu00H5ILhZjW',
        'client_secret': 'test',
    }

    return render(request, template, context)
