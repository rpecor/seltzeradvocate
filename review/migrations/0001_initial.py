# Generated by Django 2.2 on 2019-04-14 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seltzer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('abv', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('smell', models.DecimalField(decimal_places=2, max_digits=3)),
                ('taste', models.DecimalField(decimal_places=2, max_digits=3)),
                ('carbonation', models.DecimalField(decimal_places=2, max_digits=3)),
                ('overall', models.DecimalField(decimal_places=2, max_digits=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seltzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.Seltzer')),
            ],
        ),
    ]
