import random
from onestock.models import Hotels
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView, DetailView,CreateView,UpdateView
from .forms import HotelCreateForm,HotelsCreateForm
from .models import Hotels
from django.contrib.auth.forms import AuthenticationForm #login 要import
from django.core.urlresolvers import reverse
# Create your views here.
###@login_required()


class HotelsView(LoginRequiredMixin, ListView):
	template_name ='hotels/hotel_list.html'
	def get_queryset(self):
		return Hotels.objects.filter(owner=self.request.user)
	

class HotelsDetailView(LoginRequiredMixin, DetailView):
	template_name ='hotels/hotels_detail.html'
	def get_queryset(self):
		return Hotels.objects.filter(owner=self.request.user)

class HotelCreatelView(LoginRequiredMixin, CreateView):
	form_class = HotelsCreateForm
	login_url = '/login/'
	template_name ='from.html'
	#success_url = "/hotelview/"



	def  form_valid(self, form):
          instance = form.save(commit=False)
          instance.owner = self.request.user
    	  #instance.save()
          return super(HotelCreatelView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(HotelCreatelView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Hotel'
		return context
    
	"""docstring for ClassName"""

class HotelUpdateView(LoginRequiredMixin, UpdateView):
	form_class = HotelsCreateForm
	login_url = '/login/'
	#template_name ='form.html'
	template_name ='hotels/hotel-update.html'
	#success_url = "/hotelview/"

	def get_context_data(self, *args, **kwargs):
		context = super(HotelUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = f'Update Hotel: {name}'
		return context

	def get_queryset(self):
		return Hotels.objects.filter(owner=self.request.user)
    
	
	