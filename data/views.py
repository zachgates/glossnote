from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from data.models import Post


def post(request, post_id):
	try:
		post = Post.objects.get(id=post_id)
		return HttpResponse(status=200)
	except ObjectDoesNotExist:
		return HttpResponse(status=404)
	except:
		return HttpResponse(status=400)