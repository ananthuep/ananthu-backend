# Generated by Django 5.1.1 on 2024-09-25 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_docters_contact_alter_registration_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='PASSWORD',
        ),
        migrations.RemoveField(
            model_name='docters',
            name='PASSWORD',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='PASSWORD',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='PASSWORD',
        ),
        migrations.AddField(
            model_name='booking',
            name='DATE_OF_BIRTH',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='docters',
            name='DATE_OF_BIRTH',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='DATE_OF_BIRTH',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='DATE_OF_BIRTH',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
