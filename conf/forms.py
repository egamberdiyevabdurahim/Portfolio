from django import forms

from common.models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'subject', 'message']
