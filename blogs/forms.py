from django import forms
from .models import BlogPost, Comment
from tours.models import Tour


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'author', 'tour',
                  'image_url', 'image',)

    title = forms.CharField(label='Title', required=True)
    content = forms.CharField(label='Add your post content here')
    image_url = forms.URLField(label='Add the image URL here or upload the '
                               'image below',
                               required=False)
    image = forms.ImageField(label='Select Image', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tours = Tour.objects.all()
        tour_names = [(tour.id, tour.get_tour_name()) for tour in tours]

        self.fields['tour'].choices = tour_names


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('writer', 'comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
