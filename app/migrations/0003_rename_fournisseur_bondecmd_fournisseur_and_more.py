# Generated by Django 4.1.4 on 2022-12-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_bondecmd_produit_remove_bondecmd_quantite_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bondecmd',
            old_name='Fournisseur',
            new_name='fournisseur',
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='solde',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
