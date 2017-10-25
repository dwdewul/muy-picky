"""muypicky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from profiles.views import ProfileFollowToggle
from django.contrib.auth.views import (LoginView, LogoutView, 
                                    PasswordResetView, PasswordResetConfirmView,
                                    PasswordResetCompleteView, PasswordResetDoneView,
                                    PasswordChangeView, PasswordChangeDoneView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurants/', include('restaurants.urls', namespace="restaurants")),
    url(r'^items/', include('menus.urls', namespace="menus")),
    url(r'^u/', include('profiles.urls', namespace="profiles")),
    url(r'^follow/$', ProfileFollowToggle.as_view(), name='follow'),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    # May want to implement custom templates, as this routes to the Django admin page
    url(r'^password-reset/$', PasswordResetView.as_view(), name="password_reset"),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
            PasswordResetConfirmView.as_view(), 
            name="password_reset_confirm"),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
