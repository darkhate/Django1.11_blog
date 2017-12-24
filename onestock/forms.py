from django import forms
from .models import Hotels
from .validators import validate_category

class HotelCreateForm(forms.Form):
    name   = forms.CharField()
    locations  = forms.CharField(required=False)
    category  = forms.CharField(required=False) 

    def clean_name(self):
    	name =self.cleaned_data.get("name")
    	if name == "Hi":
    		raise forms.ValidationError("Not a vaild name")
    	return name

class HotelsCreateForm(forms.ModelForm):
	#email             = forms.EmailField()
	#category           = forms.CharField(required=False, validators=[validate_category])
	class Meta:
		model = Hotels
		fields = [
            'name',
            'locations',
            'category',
            'slug',
		]
	

	def clean_name(self):
		name =self.cleaned_data.get("name")
		if name == "Hi":
			raise forms.ValidationError("Not a vaild name")
		return name

	#def clean_email(self):
	#	email =self.cleaned_data.get("email")
	#	if ".edu" in email:
	#		raise forms.ValidationError("Not a vaild email")
	#	return email