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
	
	def __str__(self):
		return self.title