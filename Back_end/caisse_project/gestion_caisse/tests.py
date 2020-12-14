from django.test import TestCase
from gestion_caisse.models import caisse

#Test unitaire sur le prix et la quantité des produit pour le model caisse 

class Caisse(TestCase):

#Fonction pour configurer les objets
    def setUp(self):
        caisse.objects.create(
            name='banane', price=3, quantity=5)
        caisse.objects.create(
            name='pomme', price=1, quantity=6)
        
#Fonction pour tester les prix des produits 
    def test_prix(self):
        caisse_banane = caisse.objects.get(name='banane')
        caisse_apple = caisse.objects.get(name='pomme')
        self.assertEqual(
            caisse_banane.get_prix(), "le prix de banane est 3 €")
        self.assertEqual(
            caisse_apple.get_prix(), "le prix de pomme est 1 €")

#Fonction pour tester les Quantitées des produits 
    def test_quantity(self):
        Q_banane = caisse.objects.get(name='banane')
        Q_apple = caisse.objects.get(name='pomme')
        self.assertEqual(
            Q_banane.get_quantity(), "la quantité du banane est 5 Kg")
        self.assertEqual(
            Q_apple.get_quantity(), "la quantité du pomme est 6 Kg")