from django.db import models
from django import forms

    
class caisse(models.Model):

    id = models.AutoField(db_column='id', primary_key=True)  
    name = models.CharField(db_column='name', max_length=255)  
    price = models.IntegerField(db_column='price')  
    pictureUrl = models.CharField(db_column='pictureUrl', max_length=1000)
    quantity = models.IntegerField(db_column='quantity')
    def get_prix(self):
        self.price=str(self.price)
        return 'le prix de '+self.name + ' est ' + self.price + ' €'
    
    def get_quantity(self):
        self.quantity=str(self.quantity)
        return 'la quantité du '+self.name + ' est ' + self.quantity + ' Kg'

    class Meta:
        managed = True

        db_table = 'caisse'
        
class caisseForm(forms.ModelForm):
    class Meta:
        model = caisse
        fields="__all__"

    

class panier(models.Model):
    idp = models.AutoField(db_column='idp', primary_key=True)
    names = models.CharField(db_column='names', max_length=255) 
    quantité = models.IntegerField(db_column='quantité')
    total = models.IntegerField(db_column='total')
    
    class Meta:
        managed = True
        db_table = 'panier'
        
        
 
class order(models.Model):
    productOrders = models.ForeignKey(caisse, on_delete=models.CASCADE)    
    class Meta:
        managed = True
        db_table = 'order'
