"""mystock URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from onestock.views import (
    hotels_list,
    HotelsView,
    HotelsDetailView,
    hotel_createview,
    HotelCreatelView,
    hotel_createview,
    )   
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/$', TemplateView.as_view(template_name='Home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^hotel/$', hotels_list),
    #url(r'^hotelview/$', HotelsView.as_view(), name='hotels'),
    url(r'^hotelview/', include('onestock.urls', namespace='onestock')), # include(import application.urls, namespace='application')
    url(r'^items/', include('menus.urls', namespace='menus')),
    #url(r'^hotelview/create/$',hotel_createview),
    #url(r'^hotelview/create/$',HotelCreatelView.as_view(), name='hotels-create'),#HotelCreatelView.as_view()
    #url(r'^hotelview/(?P<slug>\w+)/$', HotelsView.as_view()),
    #url(r'^hotelview/(?P<slug>[\w-]+)/$', HotelsDetailView.as_view(), name='hotels-detail'),
    url(r'^login/$',LoginView.as_view(), name='login'),
]
