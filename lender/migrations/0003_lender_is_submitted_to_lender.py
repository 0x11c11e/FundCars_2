# Generated by Django 4.2.1 on 2023-05-11 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lender', '0002_lender_lender_apr'),
    ]

    operations = [
        migrations.AddField(
            model_name='lender',
            name='is_submitted_to_lender',
            field=models.BooleanField(default=False),
        ),
    ]
