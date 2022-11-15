from django.db import models


class Mail(models.Model):
    mail = models.EmailField(max_length=100)
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.mail}, {self.text}'
