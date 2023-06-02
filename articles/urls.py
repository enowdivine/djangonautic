from django.urls import path, re_path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.article_list, name="list"),
    path("create", views.article_create, name="create"),
    path("delete/<id>", views.article_delete, name="delete"),
    re_path(r"^(?P<slug>[\w-]+)/$", views.article_detail, name="article_detail"),
]
