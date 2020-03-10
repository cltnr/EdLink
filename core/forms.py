from django import forms


class LinkAdd(forms.Form):
    target = forms.URLField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "en.wikipedia.org/wiki/Saturn"}
        ),
    )

    link = forms.CharField(
        min_length=2,
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "saturn"}),
    )

