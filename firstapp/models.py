from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Data(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
