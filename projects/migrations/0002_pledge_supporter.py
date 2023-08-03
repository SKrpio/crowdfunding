# Generated by Django 4.2.3 on 2023-08-01 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='supporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
