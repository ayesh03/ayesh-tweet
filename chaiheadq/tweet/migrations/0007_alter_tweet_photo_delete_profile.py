# Generated by Django 5.2.1 on 2025-06-01 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
