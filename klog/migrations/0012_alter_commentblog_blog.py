# Generated by Django 4.1 on 2023-05-13 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klog', '0011_remove_commentpost_image_remove_commentpost_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentblog',
            name='Blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='klog.blog'),
        ),
    ]
