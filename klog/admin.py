from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(PostCategory)
admin.site.register(CommentPost)
admin.site.register(BlogComment)