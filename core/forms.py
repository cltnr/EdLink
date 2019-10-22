from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class LinkAdd(forms.Form):
    link = forms.CharField(
        min_length=2,
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Lien raccourci..."})
    )

    url = forms.CharField(
        min_length=3,
        max_length=200,
        widget=forms.TextInput(attrs={"placeholder": "URL"})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('link', css_class='form-group col-xs-2'),
                Column('url', css_class='form-group col-xs-2')
            )
        )

