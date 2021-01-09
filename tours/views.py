from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Tour, Category


def all_tours(request):

    tours = Tour.objects.all()
    query = None
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        tours = tours.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    context = {
        'tours': tours,
        'search_text': query,
        'current_categories': categories,
    }

    return render(request, 'tours/tours.html', context)


def indv_tour(request, tour_id):
    """ A view to show individual tour details """

    tour = get_object_or_404(Tour, pk=tour_id)

    context = {
        'tour': tour,
    }

    return render(request, 'tours/indv_tour.html', context)
