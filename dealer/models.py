from django.db import models

# Create your models here.
class Deal(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=1)
    social_security_number = models.CharField(max_length=9)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    vin = models.CharField(max_length=17, default='')
    mileage = models.IntegerField(default=0)
    year = models.CharField(max_length=4, default='')
    make = models.CharField(max_length=200, default='')
    model = models.CharField(max_length=200, default='')
    trim = models.CharField(max_length=200, default='')
    msrp = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=200, default='Pending')
    apr = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    color = models.CharField(max_length=200, default='')
    condition = models.CharField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_submitted_to_lender = models.BooleanField(default=False)
    is_approved_by_lender = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = 'Deals'
        ordering = ['last_name']


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name_plural = 'Documents'
        ordering = ['uploaded_at']