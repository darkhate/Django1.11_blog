from django import forms
from onestock.models import Hotels
from .models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields =[
		    'hotel',
		    'name',
		    'contents',
		    'excludes',
		    'public',
		]

	def __init__(self, user=None, *args, **kwargs):
		#print(kwargs.pop('user'))
		print(user)
		#print(kwargs.pop('instance'))
		super(ItemForm, self).__init__(*args,**kwargs)
		self.fields['hotel'].queryset = Hotels.objects.filter(owner=user)

