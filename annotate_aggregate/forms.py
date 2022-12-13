from django import forms


class Mail(forms.Form):
    mail = forms.EmailField(label='You email')
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "10"}))
