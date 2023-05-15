from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def dealer(request):
    return render(request, 'dealer/index.html')

def lender(request):
    return render(request, 'lender/index.html')