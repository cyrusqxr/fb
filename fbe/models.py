from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Invitation(models.Model):
	sex=models.IntegerField(default=0)
	target=models.IntegerField(default=0)
	email=models.CharField(max_length = 50)
	content=models.CharField(max_length = 100)
	#accept_email = models.CharField(max_length = 50)
	time = models.CharField(max_length = 50)
class Accept(models.Model):
	email=models.CharField(max_length = 50)
	accept_email = models.CharField(max_length = 50)
	time = models.CharField(max_length = 50)
	
class Oneword(models.Model):
	sex=models.IntegerField(default=0)
	target=models.IntegerField(default=0)	
	oneword=models.CharField(max_length = 100)	 

  		    