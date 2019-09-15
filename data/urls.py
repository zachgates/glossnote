from django.conf.urls import url

from data import views


urlpatterns = [
	url(r'^(?P<username>\w+)/$', views.posts),
	url(r'^(?P<username>\w+)/(?P<post_id>[a-zA-Z0-9]{32})/', views.post),
]
