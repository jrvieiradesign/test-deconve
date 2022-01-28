from django.db import models

from django.db import models


class Urls(models.Model):
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField('date published')
# Create your models here.
