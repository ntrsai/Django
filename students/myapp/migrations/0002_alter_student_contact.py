# Generated by Django 5.0.6 on 2024-07-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Contact',
            field=models.CharField(max_length=15),
        ),
    ]
