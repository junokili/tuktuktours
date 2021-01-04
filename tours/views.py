from django.shortcuts import render

from .models import Tour


def all_tours(request):

    tours = Tour.objects.all()

    context = {
        'tours': tours,
    }

    return render(request, 'tours/tours.html', context)
