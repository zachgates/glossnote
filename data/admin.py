from django.contrib import admin

from data.models import Post


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'id']


admin.site.register(Post, PostAdmin)
