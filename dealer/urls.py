from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deals', views.deals, name='index'),
    path('deal/<int:deal_id>/', views.deal_detail, name='deal_detail'),
    path('choose_lenders', views.choose_lenders, name='choose_lenders'),
    path('submit_to_lenders/<int:deal_id>', views.submit_to_lenders, name='submit_to_lenders'),
    path('deals_pending', views.deals_pending, name='deals_pending'),
    path('show_approved_deals', views.show_approved_deals, name='show_approved_deals'),
    path('show_approved_deal_details/<int:deal_id>', views.show_approved_deal_details, name='show_approved_deal_details'),
    path('upload/', views.upload_file_view, name='upload_file'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
