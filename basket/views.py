from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from tours.models import Tour

# Create your views here.


def view_basket(request):

    return render(request, 'basket/basket.html')


def add_to_basket(request, tour_id):

    tour = Tour.objects.get(pk=tour_id)
    tour_id = int(tour_id)
    quantity = int(request.POST.get('quantity'))
    tour_date = request.POST.get('tour_date')
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if tour_date:
        if tour_id in list(basket.keys()):
            basket[tour_id][tour_date] += quantity
            messages.success(request, f'Updated {tour.name} on {tour_date} for {quantity} \
                                people')
        else:
            basket[tour_id] = {tour_date: quantity}
            messages.success(request, f'Added {tour.name} on {tour_date} for {quantity} \
                                people to your shopping basket')
    else:
        messages.error(request, 'Please choose a date')

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
        messages.success(request, f'Removed {tour.name} from your shopping basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, tour_id):

    try:
        tour = get_object_or_404(Tour, pk=tour_id)
        basket = request.session.get('basket', {})

        basket.pop(tour_id)
        messages.success(request, f'Removed {tour.name} from your shopping basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
