from django.shortcuts import render

from .models import Lender
from dealer.models import Deal

def index(request):
    return render(request, 'lender/index.html')

def deals_list(request):
    deals_list = Deal.objects.filter(is_submitted_to_lender=True)
    return render(request, 'lender/incoming_deals.html', {'deals': deals_list})

def deal_detail(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'lender/incoming_deal_detail.html', {'deal': deal})

def approve_deal(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    deal.is_approved_by_lender = True
    deal.save()
    return render(request, 'lender/approved.html', {'deal': deal})