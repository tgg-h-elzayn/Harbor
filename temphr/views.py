from django.shortcuts import render,get_object_or_404
from .models import Candidate, Skill
from django.utils import timezone
# Create your views here.
def candidate_list(request):
	candidates = Candidate.objects.filter(join_date__lte=timezone.now()).order_by('join_date')
	return render(request, 'temphr/candidate_list.html',{'candidates': candidates})

def candidate_profile(request,pk):
	cand = get_object_or_404(Candidate,pk=pk)
	return render(request, 'temphr/candidate_profile.html',{'candidate': cand})