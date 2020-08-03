from django.forms import ModelForm
from .models import *
from django import forms



# class MieterpersonForm(forms.ModelForm):
#     class Meta:
#         model = Mieterperson
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(MieterpersonForm, self).__init__(*args, **kwargs)



class MieterpersonForm(forms.ModelForm):
	class Meta:
		model = Mieterperson
		exclude = ['mieter',]
		
class NebenmieterForm(forms.ModelForm):
	class Meta:
		model = Nebenmieter
		exclude = ['mieter',]


class WunschwohnungForm(forms.ModelForm):
	class Meta:
		model = Wunschwohnung
		exclude = ['mieter', 'aktiv']

class DocumentsForm(forms.ModelForm):
	class Meta:
		model = Documents
		exclude = ['mieter',]