# Generated by Django 4.2.3 on 2023-08-01 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('goal', models.IntegerField()),
                ('image', models.URLField()),
                ('is_open', models.BooleanField()),
                ('date_created', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.project')),
            ],
        ),
    ]
