# Generated by Django 2.0 on 2018-10-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181020_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='blog',
        ),
        migrations.DeleteModel(
            name='ReadNum',
        ),
    ]