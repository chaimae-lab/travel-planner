# Generated by Django 5.1.7 on 2025-03-15 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0006_remove_profilvoyageur_bio_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TypeVoyage',
        ),
    ]
