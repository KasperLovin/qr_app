from django import forms

class UrlForm(forms.Form):
    this_url = forms.CharField(label='text', max_length=100, required=True)