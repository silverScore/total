# Generated by Django 4.1.6 on 2023-02-08 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='care',
            options={'ordering': ['-ratingGrade']},
        ),
    ]
