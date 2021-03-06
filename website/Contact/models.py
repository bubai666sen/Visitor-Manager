from django.db import models
from django.utils import timezone
# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    subject = models.CharField(max_length = 255)
    message = models.TextField()
    TYPES = [
        ('Contact', 'Contact'),
        ('Feedback', 'Feedback'),
        ('Visiting Request', 'Visiting Request'),
        ('Report', 'Report'),
        ('Offer', 'Offer'),
    ]
    typ = models.CharField(
        max_length=45,
        choices=TYPES,
        default='Contact',
        verbose_name = "Type"
    )
    STATUS = [
        ('New', 'New'),
        ('Read', 'Read'),
        ('Inactive', 'Inactive'),
    ]
    status = models.CharField(
        max_length=45,
        choices=STATUS,
        default='New',
    )
    purpose = models.CharField(max_length = 255,default="N/A")
    # created_at = models.DateTimeField(default=timezone.now())
    # updated_at = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Message, self).save(*args, **kwargs)

    def __str__(self):  # __unicode__ for Python 2
        return self.name + ' : ' + self.subject + ' (' + self.typ + ")"

class SiteContact(models.Model):
    email = models.EmailField(max_length=255,null=True, blank=True)
    phone = models.CharField(max_length = 255,null=True, blank=True)
    short_address = models.CharField(max_length = 255,null=True, blank=True)
    long_address = models.TextField(null=True, blank=True)
    # copyright_text = models.CharField(max_length = 255,null=True)
    # powered_by_text = models.CharField(max_length = 255,null=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.email + ' (Only first row will be considered)'