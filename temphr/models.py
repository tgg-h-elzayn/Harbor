from django.db import models

# Create your models here.

class Candidate(models.Model):
	name = models.CharField(max_length=200)
	rating = models.DecimalField(decimal_places=2, max_digits=3)

class Skill(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(Candidate)