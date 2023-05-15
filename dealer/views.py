from django.shortcuts import render

from .models import Deal
from .forms import DocumentForm
from lender.models import Lender

def index(request):
    return render(request, 'dealer/index.html')

def deals(request):
    deals = Deal.objects.all()
    return render(request, 'dealer/deals.html', {'deals': deals})

def deal_detail(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'dealer/deal_detail.html', {'deal': deal})

def choose_lenders(request):
    lenders = Lender.objects.all()
    return render(request, 'dealer/choose_lenders.html', {'lenders': lenders})

def submit_to_lenders(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    deal.is_submitted_to_lender = True
    deal.save()
    return render(request, 'dealer/submit_to_lenders.html')

def deals_pending(request):
    deals = Deal.objects.filter(is_submitted_to_lender=True, is_approved_by_lender=False)
    return render(request, 'dealer/deals_pending.html', {'deals': deals})

def show_approved_deals(request):
    deals = Deal.objects.filter(is_approved_by_lender=True)
    return render(request, 'dealer/show_approved_deals.html', {'deals': deals})


def show_approved_deal_details(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    return render(request, 'dealer/show_approved_deal_details.html', {'deal': deal})

def upload_file_view(request):
    print('upload_file_view')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'dealer/success.html')
    else:
        form = DocumentForm()
    return render(request, 'dealer/upload.html', {'form': form})