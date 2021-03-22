from django import forms


class ContactForm(forms.Form):
    name=forms.CharField()
    family=forms.Charfield()
    email=forms.EmailField()
    message=forms.CharField()