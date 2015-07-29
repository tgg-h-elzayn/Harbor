from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Candidate(models.Model):
	user = models.ForeignKey(User, related_name="user_candidate")
	name = models.CharField(max_length=200)
	rating = models.DecimalField(decimal_places=2, max_digits=3)
	join_date = models.DateTimeField(default = timezone.now)
	self_description = models.TextField(default = "")
	def join(self):
		self.join_date = timezone.now()
		self.save()
	def __str__(self):
		return self.name	
class Employer(models.Model):
	user = models.OneToOneField(User, related_name="user_employer")
	name = models.CharField(max_length=200)
	def __str__(self):
		return str(self.name)
class Skill(models.Model):
	name = models.CharField(max_length=200)
	user = models.ForeignKey(Candidate)
	def add_skill(self):
		self.save()
	def __str__(self):
		return str(self.name)
class Review(models.Model):
	reviewer = models.ForeignKey(Employer)
	target = models.ForeignKey(Candidate)
	review_text = models.TextField(default="")
	rating = models.DecimalField(decimal_places=2, max_digits=3)
	def __str__(self):
		return str(self.review_text[0:20])

class Job(models.Model):
	employer = models.ForeignKey(Employer)
	employee = models.ForeignKey(Candidate)
	position = models.TextField(default="")
	price = models.DecimalField(decimal_places=2, max_digits=6)
	startDate = models.DateTimeField()
	endDate = models.DateTimeField()

	def __str__(self):
		return str(self.employer) + ": " +str(self.employee) + " as " + str(self.position) + " from " + str(self.startDate)+" to" +str(self.endDate)
