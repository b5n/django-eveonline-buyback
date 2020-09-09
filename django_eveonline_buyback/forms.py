from django import forms


class EveBuyback(forms.Form):
    submission = forms.CharField(widget=forms.Textarea)
