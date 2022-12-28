from django import forms
from django.core.validators import RegexValidator


class LinkAdd(forms.Form):
    target = forms.URLField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "en.wikipedia.org/wiki/Saturn",
            }
        ),
    )

    link = forms.CharField(
        min_length=2,
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "saturn"}
        ),
        validators=[
            RegexValidator(
                "[a-zA-Z0-9]",
                message="Short link must use 2 to 15 alphanumerical characters",
            )
        ],
    )
