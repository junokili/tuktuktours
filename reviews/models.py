from django.db import models
from tours.models import Tour
from profiles.models import UserProfile


class Review(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reviews')
    tour = models.ForeignKey(Tour, null=False, blank=False,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=False, blank=True)
    author = models.CharField(max_length=50, null=False, blank=False,
                              default='')
    review_content = models.TextField()
    review_rating = models.IntegerField(null=False, blank=False, default=0)
    writtenon = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
