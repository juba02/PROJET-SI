from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('produit/', views.produits, name='produit'),
    path('produit/<int:pk>/', views.voir, name='voir'),
    path('produit/AjoutProduit/', views.ajoutprd, name='ajoutprd'),
    path('produit/<int:pk>/Supprimer', views.supprime_prd, name='supprime_prd'),
    path('produit/<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path("produit/recherche produit/", views.rechercher_produits, name='recherche_produit'),
    path('TypeProduit/', views.type, name='TypeProduit'),
    path('TypeProduit/AjoutType', views.AjoutType, name='AjoutType'),
    path('TypeProduit/<int:pk>/Supprimer', views.supprime_type, name='supprime_type'),
    path('TypeProduit/<int:pk>/modifier/', views.modifier_type, name='modifier_type'),
    path("TypeProduit/recherche type/", views.rechercher_type, name='recherche_type'),
    path('Fournisseurs/', views.fournisseurs, name='fournisseurs'),
    path('Fournisseurs/Ajout_fournisseur/', views.Ajout_fournisseur, name='Ajout_fournisseur'),
    path('Fournisseurs/<int:pk>/supprime_fournisseur/', views.supprime_fournisseur, name='supprime_fournisseur'),
    path('Fournisseurs/<int:pk>/modifier_fournisseur/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path("Fournisseurs/recherche fournisseurs/", views.rechercher_fournisseur, name='recherche_fournisseur'),
    path("Entree/", views.Entree, name="Entree"),
    path("Bon De Commande/", views.affiche_BonDeCmd, name="BonDeCmd"),
    path("Bon De Commande/Ajout_BonDeCmd", views.ajouter_bon_de_commande, name="Ajout_BonDeCmd"),
    path("Bon De Commande/Ajout_BonDeCmd/<int:pk>/supprime_Bon_De_Commande", views.supprime_bon, name="supprime_bon"),
    path("Bon De Commande/Ajout_BonDeCmd/<int:pk>/details_Bon_De_Commande", views.details_bon, name="details_bon"),
    path('bon-de-commande/add-ligne/', views.new_form_field, name='new_form_field'),

]