# Generated by Django 5.0.6 on 2024-09-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='safetynotificationreport',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
