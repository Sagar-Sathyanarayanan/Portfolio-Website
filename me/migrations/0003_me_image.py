# Generated by Django 3.0.6 on 2020-05-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20200518_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
