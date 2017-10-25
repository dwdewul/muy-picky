from django.conf.urls import url

from .views import ItemCreateView, ItemDetailView, ItemListView, ItemUpdateView

urlpatterns = [
    url(r'^$', ItemListView.as_view(), name="items"),
    url(r'^create/$', ItemCreateView.as_view(), name="item_create"),
    url(r'^(?P<pk>[\w-]+)/$', ItemDetailView.as_view(), name="item_detail"),
    url(r'^update/(?P<pk>[\w-]+)/$', ItemUpdateView.as_view(), name="item_update"),
]