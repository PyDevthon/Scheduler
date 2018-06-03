# Generated by Django 2.0 on 2018-06-03 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0002_auto_20180603_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='added_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='interviewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviewed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]