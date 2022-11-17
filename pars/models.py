from django.db import models


class Author(models.Model):
    name = models.CharField()


class Quote(models.Model):
    quote = models.CharField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
