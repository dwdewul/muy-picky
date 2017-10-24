from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from .forms import RestaurantCreateForm

class RestaurantListView(ListView):
    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
                )
        else:
            queryset = Restaurant.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantCreateForm
    login_url = '/login/'
    template_name = 'restaurants/form.html'
    # success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreateView, self).form_valid(form)