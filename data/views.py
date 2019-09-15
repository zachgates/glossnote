import textblob

from django.http import HttpResponse
from django.shortcuts import render

from data.models import Post


def get_sentence_tags(sentence):
	tags = (tag for tag in sentence.tags)
	cur_tag = next(tags)

	for token in sentence.tokens:
		if cur_tag[0] == token:
			yield cur_tag
			try:
				cur_tag = next(tags)
			except StopIteration:
				continue
		else:
			yield (token, 'NA')


def post(request, post_id):
	try:
		post = Post.objects.get(id=post_id)
		blob = textblob.TextBlob(post.content)
		## tags = [get_sentence_tags(sentence) for sentence in blob.sentences]
		return render(request, 'data/post.html', {'post': post, 'tags': blob.sentences})
	except:
		return HttpResponse(status=404)