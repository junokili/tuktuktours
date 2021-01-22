from django import forms
from .models import Tour, Category, Review, Rating
from .widgets import CustomClearableFileInput


class TourDetailForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


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
