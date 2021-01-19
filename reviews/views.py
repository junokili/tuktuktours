from django.shortcuts import render
from .models import Review

# Create your views here.


def all_reviews(request):

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)
