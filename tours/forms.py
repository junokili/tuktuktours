from django import forms
from .models import Tour, Category, Review, Rating
from .widgets import CustomClearableFileInput


class TourDetailForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = ('name',
                  'category',
                  'sku',
                  'description',
                  'includes',
                  'price',
                  'duration',
                  'start_time',
                  'image_url',
                  'image',
                  )

    name = forms.CharField(label='Tour Name (e.g. Mojokerto Market Tour)')
    sku = forms.CharField(label='Create new sku (e.g. tt00025)')
    description = forms.CharField(label='Description (give details about '
                                  'what you will see or do, with '
                                  'some historical background)')
    price = forms.DecimalField(label='Price (e.g. $25.00)')
    duration = forms.DecimalField(label='Duration in hours (e.g. 2.5)')
    start_time = forms.CharField(label='Pick up time from hotel (e.g. 8am)')
    includes = forms.CharField(label='List what is included (e.g. Tuktuk '
                               'driver and guide, entrance fees, '
                               'mineral water etc.)')
    image_url = forms.URLField(label='Add the image URL here or upload the '
                               'image below (file should be 640 x 480px)',
                               required=False)
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'review_content',
                  'review_emoji', 'author',)

        placeholders = {
            'title': 'Give your review a short title',
            'review_content': 'Your Review',
            'review_emoji': 'Your Rating',
            'author': 'Your Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ratings = Rating.objects.all()
        names = [(rating.id, rating.get_rating_name()) for rating in ratings]

        self.fields['review_emoji'].choices = names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
