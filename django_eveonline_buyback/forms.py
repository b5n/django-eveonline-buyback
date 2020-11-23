from django import forms
from django.forms import ModelForm
from .models import BuybackSettings

class EveBuyback(forms.Form):
    submission = forms.CharField(widget=forms.Textarea)

class EveBuybackSettingsForm(ModelForm):
    class Meta:
        model = BuybackSettings 
        fields = '__all__'