from django.shortcuts import render
from .models import Comment

# Create your views here.


def all_comments(request):

    comments = Comment.objects.all()

    context = {
        'comments': comments,
    }

    return render(request, 'comments/comments.html', context)
