from django.db import models

from django.utils import timezone


class Mail(models.Model):
    mail = models.EmailField(max_length=100)
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.mail}, {self.text}'
