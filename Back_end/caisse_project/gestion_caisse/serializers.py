from rest_framework import serializers 
from .models import caisse,panier,order
#affichage de tous les reunion 
class CaisseSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = caisse
        fields = "__all__"
        
        
class PanierSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = panier
        fields = "__all__"
        
class OrderSerializer (serializers.ModelSerializer): 
    class Meta : 
        model = order
        fields = "__all__"
        
        
