# Generated by Django 4.0.5 on 2022-08-10 23:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instalaciones',
            name='texto',
        ),
        migrations.RemoveField(
            model_name='nosotros',
            name='texto',
        ),
        migrations.AddField(
            model_name='instalaciones',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nosotros',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
