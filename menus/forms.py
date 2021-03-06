from django import forms
from restaurants.models import Restaurant

from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['restaurant', 'name', 'contents', 'excludes', 'public']

    def __init__(self, user=None, *args, **kwargs):
        print(user)
        # print(kwargs)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['restaurant'].queryset = Restaurant.objects.filter(owner=user)