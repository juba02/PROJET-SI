# Generated by Django 4.1.4 on 2022-12-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_fournisseur_bondecmd_fournisseur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit_bondecmd',
            name='produit',
        ),
        migrations.AddField(
            model_name='produit_bondecmd',
            name='produit',
            field=models.ManyToManyField(to='app.produit'),
        ),
    ]
