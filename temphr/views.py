from django.shortcuts import render,get_object_or_404, redirect
from .models import Candidate, Skill
from django.utils import timezone
from .forms import CandidateForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def candidate_list(request):
	candidates = Candidate.objects.filter(join_date__lte=timezone.now()).order_by('join_date')
	return render(request, 'temphr/candidate_list.html',{'candidates': candidates})

def candidate_profile(request,pk):
	cand = get_object_or_404(Candidate,pk=pk)
	return render(request, 'temphr/candidate_profile.html',{'candidate': cand})
def candidate_new(request):
	if not request.user or request.user.is_anonymous():
		request.user = authenticate(username="h_elzayn", password='hadi')
	request.rating=0
	if request.method=="POST":
		form = CandidateForm(request.POST)
		if form.is_valid():
			cand = form.save(commit=False)
			cand.name = request.POST.get('name')
			cand.rating = 0
			cand.join_date = timezone.now()
			cand.user=authenticate(username="h_elzayn", password='hadi')
			cand.save()
			return redirect('temphr.views.candidate_profile',pk=cand.pk)
	else:
		form = CandidateForm()
	return render(request, 'temphr/candidate_edit.html',{'form':form})
