from django.forms import ModelForm

from .models import *


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class PostCategoryForm(ModelForm):
    class Meta:
        model = PostCategory
        fields = "__all__"