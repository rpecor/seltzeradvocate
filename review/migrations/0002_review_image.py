# Generated by Django 2.2 on 2019-04-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(default='default_seltzer.jpg', upload_to='seltzer_pics'),
        ),
    ]
