from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from tours.models import Tour
from .models import OrderLineItem, Order
from basket.contexts import basket_contains
import stripe
import json


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for tour_id, quantity in basket.items():
                try:
                    tour = Tour.objects.get(id=tour_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        tour=tour,
                        tour_count=quantity,
                    )
                    order_line_item.save()

                except Tour.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your shopping basket wasn't found in our database. "
                        "Please call or email us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('successful_checkout', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your shopping basket is currently empty")
            return redirect(reverse('tours'))

    current_basket = basket_contains(request)
    total = current_basket['grand_total']
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def successful_checkout(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/successful_checkout.html'
    context = {
        'order': order,
    }

    return render(request, template, context)