# Generated by Django 4.1 on 2023-04-08 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klog', '0002_postcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]