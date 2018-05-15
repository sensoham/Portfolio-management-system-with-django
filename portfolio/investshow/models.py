from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	date = models.DateTimeField()
	title = models.CharField(max_length=200)
	desc = models.TextField()
	perc_change = models.FloatField(default=0.0)
	fundsent = models.CharField(max_length=10)
	
	def __str__(self):
		return self.title
	