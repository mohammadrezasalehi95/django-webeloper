from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(required=False)
    title = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True, min_length=10, max_length=250)
