# Generated by Django 5.1.1 on 2024-09-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docters',
            name='CONTACT',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='registration',
            name='AGE',
            field=models.IntegerField(),
        ),
    ]
