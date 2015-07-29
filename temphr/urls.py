from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.candidate_list, name='candidate_list'),
	url(r'^candidate_profile/(?P<pk>[0-9]+)/$', views.candidate_profile, name = 'candidate_profile')
]