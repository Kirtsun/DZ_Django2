from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import Mail
from .tasks import send_mail as mail_send_mail


def send_mail(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            from_mail = form.cleaned_data['mail']
            text = form.cleaned_data['text']
            subject = 'Reminder'
            time = form.cleaned_data['time']
            print(timezone.now(), time)
            mail_send_mail.apply_async((subject, from_mail, text), ete=time)
            return redirect('mail:send_mail')
    else:
        form = Mail()
    return render(request, 'mail/send_mail.html', {'form': form})
