from django.shortcuts import render
from tours.models import Tour

# Create your views here.


def index(request):

    tours = Tour.objects.all()

    context = {
        'tours': tours,
    }

    return render(request, 'home/index.html', context)
