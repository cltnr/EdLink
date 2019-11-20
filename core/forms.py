from django import forms


class LinkAdd(forms.Form):
    link = forms.CharField(
        min_length=2,
        max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Lien raccourci..."})
    )

    url = forms.CharField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "URL"})
    )
