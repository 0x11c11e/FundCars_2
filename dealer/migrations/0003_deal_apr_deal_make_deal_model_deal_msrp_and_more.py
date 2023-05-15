# Generated by Django 4.2.1 on 2023-05-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_alter_deal_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='apr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='deal',
            name='make',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='deal',
            name='model',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='deal',
            name='msrp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='deal',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='deal',
            name='status',
            field=models.CharField(default='Pending', max_length=200),
        ),
        migrations.AddField(
            model_name='deal',
            name='trim',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='deal',
            name='vin',
            field=models.CharField(default='', max_length=17),
        ),
        migrations.AddField(
            model_name='deal',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]
