# Generated by Django 4.2.6 on 2023-10-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceendpoints',
            name='method',
            field=models.CharField(choices=[('POST', 'POST'), ('PUT', 'PUT'), ('GET', 'GET'), ('DELETE', 'DELETE')]),
        ),
    ]
