from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group, User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import permissions, viewsets, status as status_codes
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lender.models import Lender
from lender.serializers import LenderSerializer

from .forms import DocumentForm
from .models import Deal
from .serializers import DealSerializer, GroupSerializer, UserSerializer


def index(request):
    return render(request, 'dealer/index.html')

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


class DealsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows deal to be viewed or edited.
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    @action(detail=False, methods=['get'])
    def submit_to_lenders(self, request):
        deal_id = request.query_params.get('deal_id')
        if not deal_id:
            return Response({'error': 'deal_id is required'}, status=status_codes.HTTP_400_BAD_REQUEST)
        deal = Deal.objects.get(id=deal_id)
        deal.is_submitted_to_lender = True
        deal.save()
        return Response({'status': 'OK'}, status=status_codes.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def status(self, request):
        status_filter = request.query_params.get('status')
        if not status_filter:
            return Response({'error': 'status is required'}, status=status_codes.HTTP_400_BAD_REQUEST)
        queryset = self.get_queryset()
        
        if status_filter == 'pending':
            queryset = queryset.filter(is_submitted_to_lender=True, is_approved_by_lender=False)
        elif status_filter == 'approved':
            queryset = queryset.filter(is_submitted_to_lender=True, is_approved_by_lender=True)
        else:
            return Response({'error': 'Invalid status'}, status=status_codes.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)