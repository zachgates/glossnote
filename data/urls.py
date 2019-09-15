from django.conf.urls import url

from data import views


urlpatterns = [
	url(r'^(?P<post_id>\w+)/', views.post),
]
