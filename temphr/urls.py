from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.candidate_list, name='candidate_list')
]