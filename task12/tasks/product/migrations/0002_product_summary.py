# Generated by Django 4.1.1 on 2022-09-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is cool ok !'),
        ),
    ]
