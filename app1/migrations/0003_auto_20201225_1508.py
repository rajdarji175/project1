# Generated by Django 3.1.4 on 2020-12-25 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='name',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
