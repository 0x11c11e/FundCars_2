from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  .  import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file_view, name='upload_file'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
