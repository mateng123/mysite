# Generated by Django 2.0 on 2018-11-15 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_auto_20181104_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_time']},
        ),
    ]
