from django.shortcuts import render, redirect
from datetime import timedelta
from django.utils import timezone
from .forms import MailForm
from .tasks import send_mail as mail_send_mail


def send_mail(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            from_mail = form.cleaned_data['mail']
            text = form.cleaned_data['text']
            subject = text
            time = form.cleaned_data['time']
            a = timezone.now()
            a1 = timezone.now() + timedelta(days=2)
            if a > time or time > a1:
                pass
            else:
                time = time - a
                mail_send_mail.apply_async((subject, from_mail, text), countdown=time.seconds)
            return redirect('mail:send_mail')
    else:
        form = MailForm()
    return render(request, 'mail/send_mail.html', {'form': form})
