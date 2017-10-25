from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View

from restaurants.models import Restaurant
from menus.models import Item
from .models import Profile

User = get_user_model()

class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_to_toggle = request.POST.get("username")
        profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        user = self.request.user

        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
        return redirect(f"/u/{profile_.user.username}")

class ProfileDetailView(DetailView):
    template_name = 'profiles/user.html'

    def get_object(self):
        username = self.kwargs.get("username")
        if not username:
            raise Http404
        return get_object_or_404(User, username__iexact=username, is_active=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['user']
        
        # Add a context variable to pass to our template
        # Sees if we are currently following a user
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following

        # Filter items if they match our search query
        query = self.request.GET.get("q")
        qs = Restaurant.objects.filter(owner=user)
        items_exist = Item.objects.filter(user=user).exists()

        if query:
            qs = qs.filter(name__icontains=query)
        
        if qs.exists() and items_exist:   
            context['locations'] = qs

        return context
