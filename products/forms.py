""""module to initialize the search form"""

from django import forms


class SearchProduct(forms.Form):

    """"class to initialize the search form"""

    product = forms.CharField(label="", max_length=10, required=True, strip=False)

