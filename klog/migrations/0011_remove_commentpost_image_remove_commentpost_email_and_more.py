# Generated by Django 4.1 on 2023-05-13 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klog', '0010_commentpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentpost',
            name='Image',
        ),
        migrations.RemoveField(
            model_name='commentpost',
            name='email',
        ),
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Body', models.TextField()),
                ('Date_Created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='BlogPost', to='klog.blog')),
            ],
        ),
    ]
