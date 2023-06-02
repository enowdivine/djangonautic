from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    print(articles)
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

def article_delete(request, id=None):
    # return HttpResponse(slug)
    article = Article.objects.get(id=id)
    article.delete()
    return render(request, 'articles/delete_confirm.html')

@login_required(login_url="/accounts/login") #login reuired to create article
def article_create(request):
    if request.method == 'POST':
        form  = forms.CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})