# Generated by Django 5.0.6 on 2024-06-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_alter_createuser_email_alter_createuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createuser',
            name='phone',
            field=models.CharField(max_length=40),
        ),
    ]