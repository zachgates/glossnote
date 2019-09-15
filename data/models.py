import textblob
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	content = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	def __init__(self, *args, **kwargs):
		models.Model.__init__(self, *args, **kwargs)
		self.blob = textblob.TextBlob(self.content)

	def __str__(self):
		return self.title

	@property
	def sentences(self):
		for sentence in self.blob.sentences:
			yield sentence

	@staticmethod
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
