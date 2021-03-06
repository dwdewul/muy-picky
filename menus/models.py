from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from restaurants.models import Restaurant

class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=255)
    contents = models.TextField(help_text='separate each item by a comma')
    excludes = models.TextField(blank=True, null=True, help_text='separate each item by a comma')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated', '-timestamp']

    def get_absolute_url(self):
        return reverse('menus:item_detail', kwargs={'pk': self.pk})

    def get_contents(self):
        return self.contents.split(",")

    def get_excludes(self):
        return self.excludes.split(",")

    def __str__(self):
        return self.name