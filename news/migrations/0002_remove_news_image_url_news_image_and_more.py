# Generated by Django 5.1.1 on 2024-12-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_url',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news/images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='scheduled_date',
            field=models.DateField(default='2024-12-31'),
            preserve_default=False,
        ),
    ]
