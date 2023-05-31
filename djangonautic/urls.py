
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as articles_views # since views is above already included


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    # urlpatterns from app article
    path('articles/', include('articles.urls')),
    # urlpatterns for the accounts app
    path('accounts/', include('accounts.urls')),
    path('', articles_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns() # Add static files from assets
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Add static media from static files