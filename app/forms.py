from django.db.models import fields
from django import forms
from .models import EntreeStock, Produit, ProduitEntreeStock, TypeProduit, BonDeCmd, Produit_BonDeCmd, Fournisseur
from django.forms import formset_factory
import datetime

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields="__all__"
class TypeForm(forms.ModelForm):
    class Meta:
        model = TypeProduit
        fields="__all__"
class BonForm(forms.ModelForm):
    class Meta:
        model = BonDeCmd
        fields=['fournisseur']
class LigneBonDeCommandeForm(forms.ModelForm):
    class Meta:
        model = Produit_BonDeCmd
        fields = ['produit', 'quantite']
# LigneBonDeCommandeFormSet = formset_factory(LigneBonDeCommandeForm, extra=1)
# class LigneBonDeCommandeForm(forms.ModelForm):
#     class Meta:
#         model = Produit_BonDeCmd
#         fields = ['quantite', 'produit']
#     # Utiliser un ModelMultipleChoiceField pour sélectionner plusieurs produits
#     produit = forms.ModelMultipleChoiceField(
#         queryset=Produit.objects.all(),
#         required=True
#     )
LigneBonDeCommandeFormSet = forms.inlineformset_factory(BonDeCmd, Produit_BonDeCmd, fields=('produit', 'quantite'), extra=1)

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields="__all__"

class ProduitEntreeStockForm(forms.ModelForm):
    class Meta:
        model = ProduitEntreeStock
        fields = "__all__"

class EntreeStockForm(forms.ModelForm):
    date_e = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = EntreeStock
        fields = "__all__"