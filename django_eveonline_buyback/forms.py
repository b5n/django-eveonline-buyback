"""
MODULE DS
"""

from django import forms


class EveBuybackItemsList(forms.Form):
    """
    CLASS DS
    """
    item_list = forms.CharField(widget=forms.Textarea)
