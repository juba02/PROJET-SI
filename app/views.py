from django.shortcuts import render, redirect
from .models import EntreeStock, Produit, ProduitEntreeStock, TypeProduit, BonDeCmd, Fournisseur, Produit_BonDeCmd
from .forms import EntreeStockForm, ProduitEntreeStockForm, ProduitForm, TypeForm, BonForm, LigneBonDeCommandeFormSet, LigneBonDeCommandeForm, FournisseurForm

# Create your views here.
def acceuil(request):
    return render(request, "acceuil.html")


############Produit####################
def produits(request):
    product = Produit.objects.all()
    return render(request, 'produit.html', {"produit" : product})


def voir(request, pk):
    try:
        product = Produit.objects.get(id=pk)
        return render(request, 'voir.html', {"produit" : product})
    except Produit.DoesNotExist:
        redirect('/acceuil')

def ajoutprd(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProduitForm()
            msg = "Produit ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "AjoutProduit.html", {"form": form, "message": msg})
    else :
            form = ProduitForm()
            msg = "Remplissez tous les champs"
            return render(request, "AjoutProduit.html", {"form":form, "message":msg})

def supprime_prd(request, pk):
    produit = Produit.objects.get(id=pk)
    produit.delete()
    return redirect('produit')

def modifier_produit(request, pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('produit')
    else:
        form = ProduitForm(initial={
            'nom':produit.nom_p,
            'prix achete':produit.prix_HT,
            'prix vendu':produit.prix_vd,
            'type_produit':produit.type_produit,
            'quantite':produit.quantite
        })
    return render(request, 'modifier_produit.html', {'form': form})


def rechercher_produits (request):
    produits =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
             produits=Produit.objects.filter(nom_p__contains = query)
        return render(request, "search_p.html",{"products": produits})


##################  Type  ###############################
def type(request):
    tp = TypeProduit.objects.all()
    return render(request, 'TypeProduit.html', {"TypeProduit":tp}) 

def AjoutType(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            form = TypeForm()
            msg = "Type ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "AjoutType.html", {"form": form, "message": msg})
    else :
        form = TypeForm()
        msg = "Remplissez tous les champs"
        return render(request, "AjoutType.html", {"form":form, "message":msg})


def supprime_type(request, pk):
    type = TypeProduit.objects.get(id=pk)
    type.delete()
    return redirect('TypeProduit')


def modifier_type(request, pk):
    type = TypeProduit.objects.get(id=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('TypeProduit')
    else:
        form = TypeForm(initial={
            'nom_t':type.nom_t
        })
    return render(request, 'modifier_type.html', {'form': form})


def rechercher_type (request):
    type =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            type=TypeProduit.objects.filter(nom_t__contains = query)
        return render(request, "search_t.html",{"types": type})


#########################  Fournisseur  ################################
def fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'fournisseurs.html', {"fournisseurs": fournisseurs})

 
def Ajout_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form = FournisseurForm()
            msg = "fournisseur ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "Ajout_fournisseur.html", {"form": form, "message": msg})
    else :
        form = FournisseurForm()
        msg = "Remplissez tous les champs"
        return render(request, "Ajout_fournisseur.html", {"form":form, "message":msg})

def supprime_fournisseur(request, pk):
    fournisseur = Fournisseur.objects.get(id=pk)
    fournisseur.delete()
    return redirect('fournisseurs')

def modifier_fournisseur(request, pk):
    fournisseur = Fournisseur.objects.get(id=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('fournisseurs')
    else:
        form = FournisseurForm(initial={
            'nom_f':fournisseur.nom_f,
            'prenom_f':fournisseur.prenom_f,
            'adresse_f':fournisseur.adresse_f,
            'telephone_f':fournisseur.telephone_f,
            'solde':fournisseur.solde
        })
    return render(request, 'modifier_fournisseur.html', {'form': form})

def rechercher_fournisseur (request):
    fournisseur =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            fournisseur=Fournisseur.objects.filter(nom_f__contains = query)
        return render(request, "search_f.html",{"fournisseurs": fournisseur})

################ achat  ###################################


def Entree(request):
    return render(request, "Entree.html")
def affiche_BonDeCmd(request):
    bon = BonDeCmd.objects.all()
    return render(request, "BonDeCmd.html", {"bon":bon})
def ajouter_bon_de_commande(request):
    if request.method == 'POST':
        form = BonForm(request.POST)
        formset = LigneBonDeCommandeFormSet(request.POST, prefix='lignes')
        if form.is_valid() and formset.is_valid():
            bon_de_commande = form.save()
            lignes = formset.save(commit=False)
            for ligne in lignes:
                ligne.bon_de_commande = bon_de_commande
                ligne.save()
            return redirect('BonDeCmd')
    else:
        form = BonForm()
        formset = LigneBonDeCommandeFormSet(prefix='lignes')
    return render(request, 'Ajout_BonDeCmd.html', {
        'form': form,
        'formset': formset,
    })
# def ajouter_bon_de_commande(request):
#     if request.method == 'POST':
#         form = BonForm(request.POST)
#         formset = LigneBonDeCommandeFormSet(request.POST, prefix='lignes')
#         if form.is_valid() and formset.is_valid():
#             bon_de_commande = form.save()
#             formset.instance = bon_de_commande
#             formset.save()
#             return redirect('BonDeCmd')
#     else:
#         form = BonForm()
#         formset = LigneBonDeCommandeFormSet(prefix='lignes')
#     return render(request, 'Ajout_BonDeCmd.html', {'form': form, 'formset': formset})
# def ajouter_bon_de_commande(request):
#     if request.method == 'POST':
#         form = BonForm(request.POST)
#         formset = LigneBonDeCommandeFormSet(request.POST, prefix='lignes')
#         if form.is_valid() and formset.is_valid():
#             bon_de_commande = form.save()
#             formset.instance = bon_de_commande
#             formset.save()
#             return redirect('BonDeCmd')
#     else:
#         form = BonForm()
#         # Initialiser le formset avec la liste des produits disponibles
#         formset = LigneBonDeCommandeFormSet(prefix='lignes', queryset=Produit.objects.all())
#     return render(request, 'Ajout_BonDeCmd.html', {'form': form, 'formset': formset})


def new_form_field(request):
  if request.is_ajax():
    form = LigneBonDeCommandeForm()
    return render(request, 'new_form_field.html', {'form': form})
  else:
    return render(request, "acceuil.html")


def details_bon(request,pk):
    produit_bon = Produit_BonDeCmd.objects.filter(id__contains=pk)
    return render(request, "details_bon.html", {"produit_bon": produit_bon })
def supprime_bon(request, pk):
    bon = BonDeCmd.objects.get(id=pk)
    bon.delete()
    return redirect('BonDeCmd')


################### produitEntreeStock  #################

def produitEntreeStock(request):
    TypeProduits= TypeProduit.objects.all()
    produitsEntreeStock = ProduitEntreeStock.objects.all()
    Produits = Produit.objects.all()

    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    typeid= request.GET.get('type', '')
    produitid= request.GET.get('produit', '')

    
    if max_price:
        produitsEntreeStock = produitsEntreeStock.filter(prix_unite_ht__lte = max_price)
    if min_price:
        produitsEntreeStock = produitsEntreeStock.filter(prix_unite_ht__gte = min_price)
    if typeid:
        produitsEntreeStock = produitsEntreeStock.filter(produit__type_produit__id = typeid)
    if produitid:
        produitsEntreeStock = produitsEntreeStock.filter(produit__id = produitid)
     
    return render(request, 'etat_stock.html', {"ProduitEntreeStock": produitsEntreeStock, "TypeProduits":TypeProduits, "Produits":Produits}) 

def ajouter_produitEntreeStock(request):
    if request.method == 'POST':
        form = ProduitEntreeStockForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProduitEntreeStockForm()
            msg = "Entrée ajouter, vous pouvez ajouter un autre"
        else : 
            msg = "Remplissez tous les champs"
        return render(request, "ajouter_produitEntreeStock.html", {"form": form, "message": msg})
    else :
        form = ProduitEntreeStockForm()
        msg = "Remplissez tous les champs"
        return render(request, "ajouter_produitEntreeStock.html", {"form":form, "message":msg})


def supprimer_produitEntreeStock(request, pk):
    type = TypeProduit.objects.get(id=pk)
    type.delete()
    return redirect('TypeProduit')


def modifier_produitEntreeStock(request, pk):
    type = TypeProduit.objects.get(id=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type)
        if form.is_valid():
            form.save()
            return redirect('TypeProduit')
    else:
        form = TypeForm(initial={
            'nom_t':type.nom_t
        })
    return render(request, 'modifier_type.html', {'form': form})


def rechercher_produitEntreeStock(request):
    type =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            type=TypeProduit.objects.filter(nom_t__contains = query)
        return render(request, "search_t.html",{"types": type})



####################################################################
############## Entrée Stock ########################################
####################################################################

def entreeStock(request):
    entreeStock = EntreeStock.objects.all()
    return render(request, 'entreeStock.html', {"EntreeStock": entreeStock}) 


def ajouter_entreeStock(request):
    if request.method == 'POST':
        form = EntreeStockForm(request.POST)
        if form.is_valid():
            form.save()
            form = EntreeStockForm()
            msg = "Entrée Stock ajouté"
            return redirect("ajouter_produitEntreeStock")
        else : 
            msg = "Remplissez tous les champs"
            return render(request, "ajouter_entreeStock.html")
    else :
        form = EntreeStockForm()
        msg = "Remplissez tous les champs"
        return render(request, "ajouter_entreeStock.html", {"form":form, "message":msg})


def supprimer_entreeStock(request, pk):
    entree = EntreeStock.objects.get(id=pk)
    entree.delete()
    return redirect('entreeStock')


def modifier_entreeStock(request, pk):
    entree = EntreeStock.objects.get(id=pk)
    if request.method == 'POST':
        form = EntreeStockForm(request.POST, instance=entree)
        if form.is_valid():
            form.save()
            return redirect('entreeStock')
    else:
        form = EntreeStockForm(instance = entree)
    return render(request, 'modifier_entreeStock.html', {'form': form})


def rechercher_entreeStock(request):
    entree =""
    if (request.method =="GET"):
        query=request.GET.get('recherche')
        if query:
            entree=EntreeStock.objects.filter(date_e__contains = query)
        return render(request, "search_eStock.html", {"Entree": entree})
