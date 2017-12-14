import random
from onestock.models import Hotels
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView,ListView, DetailView,CreateView
from .forms import HotelCreateForm,HotelsCreateForm
from .models import Hotels
from django.contrib.auth.forms import AuthenticationForm #login 要import
from django.core.urlresolvers import reverse
# Create your views here.
@login_required()
def hotel_createview(request):
    form = HotelsCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
    	if request.user.is_authenticated():
    	  instance = form.save(commit=False)
    	  instance.owner = request.user
    	  instance.save()
    	  return HttpResponseRedirect("/hotelview/")
    	else:
    		return HttpResponseRedirect("registration/login/")
    if form.errors:
         print(form.errors)
         errors = form.errors

    template_name ='hotels/form.html'
    context = {"form" : form, "errors" : errors}
    return render(request,template_name,context)



def hotels_list(request,):
	template_name ='hotels/hotel_list.html'
	queryset = Hotels.objects.all()
	context = {
	     "object_list":queryset
	}
	return render(request,template_name,context)

def hotels_detailview(request, slug):
	template_name ='hotels/hotels_detail.html'
	obj = Hotels.objects.get(slug=slug)
	context = {
	     "object_list":obj
	}
	return render(request,template_name,context)

class HotelsView(ListView):
	template_name ='hotels/hotel_list.html'

	def get_queryset(self):
		slug =self.kwargs.get("slug")
		print(slug)
		if slug:
			queryset = Hotels.objects.filter(name=slug)
		else:
			queryset = Hotels.objects.all()
		return queryset

class HotelsDetailView(DetailView):
	template_name ='hotels/hotels_detail.html'
	queryset = Hotels.objects.all()

class HotelCreatelView(LoginRequiredMixin, CreateView):
	form_class = HotelsCreateForm
	login_url = '/login/'
	template_name ='form.html'
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
	
	#def get_context_data(self,*args,**kwargs):
	#	context = super(HotelsDetailView,self).get_context_data(*args,**kwargs)
	#	return context

	#def get_object(self,*args,**kwargs):
	#	rest_id = self.kwargs.get('rest_id')
	#	obj = get_object_or_404(Hotels, id=rest_id)
	#	return obj
   