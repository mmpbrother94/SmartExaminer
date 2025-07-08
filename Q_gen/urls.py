from django.contrib import admin
from django.urls import path
from Q_gen import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index,name="home"),
    path('page1.html/', views.upload_text,name="page1"),
    path('page2.html/', views.evaluate_answer,name="page2"),
    path('page1.html/index.html/', views.index,name="home"),
    path('page2.html/index.html/', views.index,name="home"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
