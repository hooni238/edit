from django import forms
from .models import pic
'''class picform(forms.Form):
    name=forms.CharField()
    pic =forms.FileField()'''
class picform(forms.ModelForm):
    class Meta:
        model = pic
        fields = (
	'name',	
	'pic')

