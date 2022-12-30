from django.db import models
from datetime import datetime



class TypeProduit(models.Model):
    nom_t = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nom_t)

class Produit(models.Model):
    nom_p = models.CharField(max_length=100)
    prix_HT = models.DecimalField(max_digits=10, decimal_places=2)
    prix_vd = models.DecimalField(max_digits=10, decimal_places=2)
    type_produit = models.ForeignKey(TypeProduit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    def __str__(self):
        return str(self.nom_p)

class Client(models.Model):
    nom_c = models.CharField(max_length=100)
    prenom_c = models.CharField(max_length=100)
    adresse_c = models.TextField()
    telephone_c = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nom_c)

class Fournisseur(models.Model):
    nom_f = models.CharField(max_length=100)
    prenom_f = models.CharField(max_length=100)
    adresse_f = models.TextField()
    telephone_f = models.CharField(max_length=20)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return str(self.nom_f +" "+ self.prenom_f)

class EntreeStock(models.Model):
    numero_e = models.CharField(max_length=20)
    date_e = models.DateField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.numero_e)

class ProduitEntreeStock(models.Model):
    entree_stock = models.ForeignKey(EntreeStock, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unite_ht = models.DecimalField(max_digits=10, decimal_places=2)

class Vente(models.Model):
    numero_v = models.CharField(max_length=20)
    date_v = models.DateField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class ProduitVente(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    prix_unite_ht = models.DecimalField(max_digits=10, decimal_places=2)
class BonDeCmd (models.Model):
    date_b = models.DateTimeField(default=datetime.now)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
class Produit_BonDeCmd (models.Model):
    bon = models.ForeignKey(BonDeCmd, on_delete=models.CASCADE)
    produit = models.ManyToManyField(Produit)
    quantite = models.PositiveIntegerField()



