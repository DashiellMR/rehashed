# Generated by Django 5.0.1 on 2024-01-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_account', '0011_alter_userprofile_partyq1_alter_userprofile_partyq2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='partyq5',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='partyq6',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gamingq1',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gamingq2',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='partyq1',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='partyq2',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='partyq3',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='partyq4',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq1',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq2',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq3',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq4',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq5',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tearsq6',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
