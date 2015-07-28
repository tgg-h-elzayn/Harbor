from django.contrib import admin
from .models import Candidate, Skill, Employer, Review, Job
# Register your models here.
admin.site.register(Candidate)
admin.site.register(Skill)
admin.site.register(Employer)
admin.site.register(Review)
admin.site.register(Job)