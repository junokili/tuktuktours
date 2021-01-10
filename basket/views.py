from django.shortcuts import render, redirect

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
    print
    return redirect(redirect_url)
