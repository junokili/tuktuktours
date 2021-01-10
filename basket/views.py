from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from tours.models import Tour

# Create your views here.


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, tour_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if tour_id in list(basket.keys()):
        basket[tour_id] += quantity
    else:
        basket[tour_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, tour_id):

    tour = get_object_or_404(Tour, pk=tour_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[tour_id] = quantity
        messages.success(request, f'Updated {tour.name} quantity to {basket[tour_id]}')
    else:
        basket.pop(tour_id)
        messages.success(request, f'Removed {tour.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, tour_id):

    try:
        basket = request.session.get('basket', {})

        basket.pop(tour_id)

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
