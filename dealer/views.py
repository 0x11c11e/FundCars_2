from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Deal
from .forms import DocumentForm
from lender.models import Lender

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import User, Group

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

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/home/")  # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            return render(request, "login.html", {"error": "Invalid login credentials"})
    else:
        return render(request, "login.html")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
