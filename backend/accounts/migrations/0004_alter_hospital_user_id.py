# Generated by Django 4.1 on 2023-06-19 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email_alter_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='user_id',
            field=models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]