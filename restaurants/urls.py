from django.conf.urls import url

from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView

urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name="restaurants"),
    url(r'^create/$', RestaurantCreateView.as_view(), name="restaurants_create"),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name="restaurant_detail"),
]