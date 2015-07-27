from django.db import models
from django.utils import timezone
# Create your models here.

class Candidate(models.Model):
	name = models.CharField(max_length=200)
	rating = models.DecimalField(decimal_places=2, max_digits=3)
	join_date = models.DateTimeField(default = timezone.now)
	
	def join(self):
		self.join_date = timezone.now()
		self.save()
	def __str__(self):
		return self.name
class Skill(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(Candidate)