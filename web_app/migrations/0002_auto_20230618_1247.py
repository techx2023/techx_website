# Generated by Django 3.2.12 on 2023-06-18 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='image',
            new_name='img_detail_page',
        ),
        migrations.AddField(
            model_name='services',
            name='back_descrption',
            field=models.TextField(blank=True, null=True, verbose_name='Description Back-end'),
        ),
        migrations.AddField(
            model_name='services',
            name='front_descrption',
            field=models.TextField(blank=True, null=True, verbose_name='Description Front-end'),
        ),
        migrations.AddField(
            model_name='services',
            name='img_service_page',
            field=models.ImageField(default=1, upload_to='Images/services', verbose_name='Image du service'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='is_home',
            field=models.BooleanField(default=False),
        ),
    ]