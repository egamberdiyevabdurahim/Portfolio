# Generated by Django 5.1.3 on 2024-11-24 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_mainmodel_name_for_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliomodel',
            name='image',
            field=models.ImageField(null=True, upload_to='test'),
        ),
    ]
