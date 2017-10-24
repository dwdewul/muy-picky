from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

class Restaurant(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:restaurant_detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('saving...')
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

# def rl_post_save_receiver(sender, instance, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=Restaurant)
# post_save.connect(rl_post_save_receiver, sender=Restaurant)