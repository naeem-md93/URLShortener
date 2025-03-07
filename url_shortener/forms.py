from django import forms


class URLForm(forms.Form):
    url = forms.URLField(max_length=1000)