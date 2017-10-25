from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from .forms import RestaurantCreateForm

class RestaurantListView(ListView):
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


class RestaurantDetailView(DetailView):
    def get_queryset(self):
        return Restaurant.objects.filter(owner=self.request.user)


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

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantCreateForm
    login_url = '/login/'
    template_name = 'restaurants/form.html'
    # success_url = '/restaurants/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context
