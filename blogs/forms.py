from django import forms
from .models import BlogPost
from tours.widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'author',
                  'image',)

        image = forms.ImageField(label='Image', required=False,
                                 widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """ add placeholders and classes"""
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Body of post',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
