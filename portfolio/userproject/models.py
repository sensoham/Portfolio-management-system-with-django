from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
	ProjectTitle = models.CharField(max_length=100)
	CommitAmount = models.FloatField(default=0.0)
	ExpectedReturn = models.FloatField(default=0.0)
	CommitDuration = models.CharField(max_length=50)
	date = models.DateTimeField(auto_now_add=True)
	SymbolChoice = models.CharField(max_length=200)
	Comments = models.TextField()
	IsUndertaken = models.BooleanField(default=False)
	author = models.ForeignKey(User, default=None)
	
	def __str__(self):
		return self.ProjectTitle
	