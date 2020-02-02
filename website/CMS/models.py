from django.db import models

# Create your models here.

class Page(models.Model):
    STATUS_CHOICES = (
        (1, 'Active'),
        (2, 'Inactive'),
    )
    PAGE_CHOICES = (
        (1, 'Home'),
        (2, 'About Us'),
    )
    page =  models.PositiveSmallIntegerField(choices=PAGE_CHOICES,unique=True)
    title = models.CharField(max_length = 255, null=True, blank=True)
    heading = models.CharField(max_length = 255, null=True, blank=True)
    short_description = models.CharField(max_length = 255, null=True, blank=True)
    long_description = models.CharField(max_length = 255, null=True, blank=True)
    image = models.ImageField(upload_to='static/uploads/cms/', null=True, blank=True)
    background_image = models.ImageField(upload_to='static/uploads/cms/', null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.title + " (" + str(self.page) + ")"