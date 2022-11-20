from datetime import timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class Mail(forms.Form):
    mail = forms.EmailField(label='You email')
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "10"}))
    time = forms.DateTimeField(initial=timezone.now)

    def clean_time(self):
        time = self.cleaned_data['time']
        if timezone.now() > time or time > timezone.now() + timedelta(days=2):
            raise ValidationError('The date cannot be in the past or two days ahead')
        return time
