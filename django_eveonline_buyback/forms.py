from django import forms


class EveBuyback(forms.Form):
    blue_loot_buyback_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    general_buyback_rate = forms.DecimalField(max_digits=5, decimal_places=2)
    item_list = forms.CharField(widget=forms.Textarea)
