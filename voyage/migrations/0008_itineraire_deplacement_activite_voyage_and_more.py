# Generated by Django 5.1.7 on 2025-03-16 05:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voyage', '0007_delete_typevoyage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jour', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Deplacement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temps_deplacement', models.CharField(max_length=50)),
                ('itineraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deplacements', to='voyage.itineraire')),
            ],
        ),
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('duree', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('itineraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activites', to='voyage.itineraire')),
            ],
        ),
        migrations.CreateModel(
            name='Voyage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('type_voyage', models.CharField(max_length=50)),
                ('date_depart', models.DateField()),
                ('date_retour', models.DateField()),
                ('critere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voyages', to='voyage.criterevoyage')),
            ],
        ),
        migrations.AddField(
            model_name='itineraire',
            name='voyage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraire', to='voyage.voyage'),
        ),
    ]
