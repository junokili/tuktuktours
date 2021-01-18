from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.db.models import Q
from django.db.models.functions import Lower
from .models import BlogPost
from .forms import BlogPostForm
from profiles.models import UserProfile


def all_posts(request):

    posts = BlogPost.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                posts = posts.annotate(lower_title=Lower('title'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posts = posts.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('blogs'))

            queries = Q(name__icontains=query) | Q(content__icontains=query)
            posts = posts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posts': posts,
        'search_text': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'blogs/posts.html', context)


def post_detail(request, post_id):
    """ A view to show individual blog post details """

    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blogs/post_detail.html', context)


def add_post(request):
    if not request.user.is_superuser:
        messages.error(request,
                       f'Sorry, you are not authorized to do that. If you would like to \
                       add a post to our site please contact us here { settings.DEFAULT_FROM_EMAIL }.')
        return redirect(reverse('posts'))

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully added new post!')
            return redirect(reverse('post_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add new post. Please ensure the form is valid.')
    else:
        form = BlogPostForm()

    try:
        profile = UserProfile.objects.get(user=request.user)
        form = BlogPostForm(initial={
            'author': profile.default_full_name,
                })
    except UserProfile.DoesNotExist:
        form = BlogPostForm()

    template = 'blogs/add_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
