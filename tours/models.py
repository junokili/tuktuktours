from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tour(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    includes = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    tour = models.ForeignKey(Tour, null=False, blank=False,
                             on_delete=models.CASCADE,
                             related_name='reviews',)
    title = models.CharField(max_length=254, null=False, blank=True)
    author = models.CharField(max_length=50, null=False, blank=False,
                              default='')
    review_content = models.TextField()
    review_emoji = models.ForeignKey('Rating', null=False, blank=False,
                                     on_delete=models.CASCADE,
                                     related_name='reviews', default='')
    writtenon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['writtenon']

    def __str__(self):
        return self.title


class Rating(models.Model):

    class Meta:
        verbose_name_plural = 'Ratings'
    rating_name = models.CharField(max_length=254, null=False, blank=False,
                                   default='')
    rating_number = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.rating_name

    def get_rating_name(self):
        return self.rating_name
