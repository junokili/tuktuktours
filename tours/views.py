from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Tour, Category
from blogs.models import BlogPost
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .forms import TourDetailForm, CategoryForm, ReviewForm


def all_tours(request):

    tours = Tour.objects.all()
    query = None
    categories = Category.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                tours = tours.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            tours = tours.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            tours = tours.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms!")
                return redirect(reverse('tours'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            tours = tours.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'tours': tours,
        'categories': categories,
        'search_text': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'tours/tours.html', context)


def indv_tour(request, tour_id):
    """ A view to show individual tour details """

    tour = get_object_or_404(Tour, pk=tour_id)
    posts = BlogPost.objects.all()
    reviews = tour.reviews.all()

    context = {
        'tour': tour,
        'posts': posts,
        'reviews': reviews,
    }

    return render(request, 'tours/indv_tour.html', context)


@login_required
def make_review(request, tour_id):

    tour = get_object_or_404(Tour, pk=tour_id)
    review_form = ReviewForm

    context = {
        'tour': tour,
        'review_form': review_form,
    }

    return render(request, 'tours/indv_tour_add_review.html', context)


@login_required
def add_review(request, tour_id):
    """ A view to add a review to an individual tour """

    tour = get_object_or_404(Tour, pk=tour_id)
    new_review = None

    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            # Create Review object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current review to the tour
            new_review.tour = tour
            # Save the review to the database
            new_review.save()
            messages.success(request, f'Thanks for reviewing the {tour.name}!')
            return redirect(reverse('indv_tour', args=[tour.id]))
    else:
        messages.error(request, 'Failed to add review. '
                       'Please ensure the form is valid.')
        review_form = ReviewForm()

    template = 'tours/indv_tour_add_review.html'
    context = {
        'tour': tour,
        'new_review': new_review,
        'review_form': review_form,
    }

    return render(request, template, context)


@login_required
def add_tour(request):
    """ Add a new tour to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TourDetailForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, f'Successfully added the new \
                             tour {tour.name}!')
            return redirect(reverse('indv_tour', args=[tour.id]))
        else:
            messages.error(request, 'Failed to add new tour. '
                           'Please ensure the form is valid.')
    else:
        form = TourDetailForm()

    template = 'tours/add_tour.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tour(request, tour_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)

    if request.method == 'POST':
        form = TourDetailForm(request.POST, request.FILES, instance=tour)
        if form.is_valid:
            form.save()
            messages.success(request, f'Successfully updated the {tour.name}')
            return redirect(reverse('indv_tour', args=[tour.id]))
        else:
            messages.error(request, 'Failed to update tour. '
                           'Check that the form entry is valid')
    else:
        form = TourDetailForm(instance=tour)
        messages.info(request, f'You are editing the {tour.name}')

    template = 'tours/edit_tour.html'
    context = {
        'form': form,
        'tour': tour,
    }

    return render(request, template, context)


@login_required
def delete_tour(request, tour_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    tour = get_object_or_404(Tour, pk=tour_id)
    tour.delete()
    messages.success(request, f'Deleted the {tour.name}')
    return redirect(reverse('tours'))


def all_categories(request):

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'tours/categories.html', context)


@login_required
def add_category(request):
    """ Add a new category to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Successfully added new category \
                             { category.friendly_name }!')
            return redirect(reverse('categories'))
        else:
            messages.error(request, 'Failed to add new category. '
                           'Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'tours/categories/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_category(request, category_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid:
            form.save()
            messages.success(request, f'Successfully updated category \
                             { category.friendly_name }')
            return redirect(reverse('categories'))
        else:
            messages.error(request, 'Failed to update category. '
                           'Check that the form entry is valid')
    else:
        form = CategoryForm(instance=category)
        messages.info(request, f'You are editing the category \
                      {category.friendly_name}')

    template = 'tours/categories/edit_category.html'
    context = {
        'form': form,
        'category': category,
    }

    return render(request, template, context)


@login_required
def delete_category(request, category_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not authorized to do that')
        return redirect(reverse('home'))

    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    messages.success(request, f'Deleted the category {category.friendly_name}')
    return redirect(reverse('categories'))
