# Generated by Django 4.1.6 on 2023-02-08 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0003_alter_care_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='care',
            options={'ordering': ['ratingDate', 'ratingGrade']},
        ),
    ]
