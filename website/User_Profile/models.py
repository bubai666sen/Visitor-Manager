from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import escape
from django.utils.html import mark_safe
#from phone_field import PhoneField

class Profile(models.Model):
    VISITOR = 1
    ADMIN = 2
    STAFF = 3
    OTHER = 4
    ROLE_CHOICES = (
        (VISITOR, 'Visitor'),
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (OTHER, 'Other'),
    )
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Active'),
        (3, 'Inactive'),
    )
    profile_id = models.CharField(max_length=100, unique=True)
    #phone = PhoneField(help_text='Contact phone number')
    phone = models.CharField(max_length=13)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True,default=1)
    company_name = models.CharField(max_length=50,default="N/A")
    image = models.ImageField(upload_to='static/uploads/profile_photos/',verbose_name="Profile Picture")
    arrival = models.DateTimeField(null=True, blank=True,verbose_name="Arrival Time")
    departure = models.DateTimeField(null=True, blank=True,verbose_name="Departure Time")
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=True, blank=True)

    def image_tag(self):
        #url = static(self.image.name)
        #return u'<img src="%s" />' % escape(self.image.name)
        #return '<img style="max-width: 800px;" src="'+self.image.name+'" />'
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = self.image.url,
            width= '400px',
            height= '400px',
            )
    )
    image_tag.short_description = 'Profile Picture Preview'
    image_tag.allow_tags = True

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile_id = uuid.uuid1().hex
        Profile.objects.create(user=instance,profile_id=profile_id)
    instance.profile.save()

