from django.shortcuts import render

import os
from .models import Lender
from dealer.models import Document
from django.conf import settings
from django.http import FileResponse
from io import BytesIO
from zipfile import ZipFile
from dealer.models import Deal
import tarfile

def index(request):
    return render(request, 'lender/index.html')

def deals_list(request):
    deals_list = Deal.objects.filter(is_submitted_to_lender=True)
    return render(request, 'lender/incoming_deals.html', {'deals': deals_list})

def approve_deal(request, deal_id):
    deal = Deal.objects.get(id=deal_id)
    deal.is_approved_by_lender = True
    deal.save()
    return render(request, 'lender/approved.html', {'deal': deal})

def download_zip(request):
    file_ids = request.GET.getlist('files')
    # documents = Document.objects.filter(id__in=file_ids)

    zip_io = BytesIO()

    with ZipFile(zip_io, 'w') as zip_file:
        # for document in documents:
        filename = 'Screenshot_2023-05-15_14-50-16_20230516185840.jpg' # document.file.name
        filepath = os.path.join(settings.MEDIA_ROOT + '/media/', filename)
        zip_file.write(filepath, arcname=filename)
        print(filename)
    
    response = FileResponse(zip_io, as_attachment=True, filename='documents.zip')
    return response

def download_tar_gz(request):
    files = Document.objects.all()

    # Create a tar.gz file
    tar_gz_name = 'documents.tar.gz'
    tar_gz_path = os.path.join(settings.MEDIA_ROOT, tar_gz_name)
    with tarfile.open(tar_gz_path, 'w:gz') as tar:
        for file in files:
            tar.add(file.file.path, arcname=os.path.basename(file.file.path))

    response = FileResponse(open(tar_gz_path, 'rb'), content_type='application/gzip')
    response['Content-Disposition'] = 'attachment; filename="%s"' % tar_gz_name
    return response
