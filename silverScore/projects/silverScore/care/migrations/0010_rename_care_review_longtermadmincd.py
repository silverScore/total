# Generated by Django 4.1.6 on 2023-02-10 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0009_rename_longtermadmincd_review_care'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='care',
            new_name='longTermAdminCd',
        ),
    ]
