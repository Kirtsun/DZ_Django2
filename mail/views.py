from django.shortcuts import render


from .forms import MailForm


def send_mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            text = form.cleaned_data['text']
            time = form.cleaned_data['time']

