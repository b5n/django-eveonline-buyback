from django import forms


class EveBuyback(forms.Form):
    item_list = forms.CharField(widget=forms.Textarea)
