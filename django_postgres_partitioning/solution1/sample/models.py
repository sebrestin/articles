from django.db import models


class Sample1(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
