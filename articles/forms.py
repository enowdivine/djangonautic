from django import forms
from . import models


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ["title", "slug", "body", "thumbnail"]
