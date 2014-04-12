from django import forms

class IdeateIdeaForm(forms.Form):
    ideateimage_store_location = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
