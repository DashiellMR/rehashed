# Generated by Django 5.0.1 on 2024-01-28 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_account', '0003_userprofile_delete_useraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='categories',
            field=models.TextField(blank=True),
        ),
    ]