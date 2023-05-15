from django.db import models

# Create your models here.
class Lender(models.Model):
    lender_name = models.CharField(max_length=100)
    lender_email = models.EmailField(max_length=100)
    lender_phone = models.CharField(max_length=100)
    lender_address = models.CharField(max_length=100)
    lender_city = models.CharField(max_length=100)
    lender_state = models.CharField(max_length=100)
    lender_zip = models.CharField(max_length=100)
    lender_apr = models.CharField(max_length=100, default='0.00')
    lender_country = models.CharField(max_length=100)
    lender_website = models.CharField(max_length=100)
    lender_logo = models.ImageField(upload_to='lender_logo', blank=True)
    lender_description = models.TextField()
    lender_created = models.DateTimeField(auto_now_add=True)
    lender_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lender_name

    class Meta:
        verbose_name_plural = 'Lenders'
        ordering = ['lender_name']