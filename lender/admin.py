from django.contrib import admin

from . import models

# Register your models here.
admin.site.site_header = "Lender Admin"
admin.site.site_title = "Lender Admin Portal"
admin.site.index_title = "Welcome to Lender Portal"

admin.site.register(models.Lender)