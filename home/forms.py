from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
