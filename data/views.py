from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import User
from data.models import Post
			

def posts(request, username):
	return HttpResponse(status=400)


def post(request, username, post_id):
	try:
		user = User.objects.get(username=username)
		post = Post.objects.get(posted_by=user, id=post_id)
		return render(request, 'data/post.html', {'post': post})
	except:
		return HttpResponse(status=404)