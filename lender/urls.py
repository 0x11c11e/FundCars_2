from django.contrib import admin
from django.urls import path
from  .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deals_list/', views.deals_list, name='deals_list'),
    path('deal_detail/<int:deal_id>/', views.deal_detail, name='deal_detail'),
    path('approve_deal/<int:deal_id>/', views.approve_deal, name='approve_deal'),
    path('download_zip/', views.download_tar_gz, name='download_zip'),
    ]
