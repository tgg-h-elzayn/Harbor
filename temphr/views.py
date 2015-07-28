from django.shortcuts import render
from .models import Candidate, Skill
from django.utils import timezone
# Create your views here.
def candidate_list(request):
	candidates = Candidate.objects.filter(join_date__lte=timezone.now()).order_by('join_date')
	return render(request, 'candidate/candidate_list.html',{'candidates': candidates})