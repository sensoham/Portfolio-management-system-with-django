from django import forms
from . import models

class CreateProject(forms.ModelForm):
	class Meta:
		model = models.Project
		fields = ['ProjectTitle', 'CommitAmount', 'ExpectedReturn', 'CommitDuration', 'SymbolChoice', 'Comments']
		
