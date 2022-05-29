from django import forms


class SearchProduct(forms.Form):
    product = forms.CharField(label="", max_length=10, required=True, strip=False)

