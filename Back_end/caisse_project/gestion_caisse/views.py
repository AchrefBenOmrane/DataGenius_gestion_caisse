from django.shortcuts import render, redirect , HttpResponseRedirect 
from gestion_caisse.models import caisse,panier,order
from rest_framework.response import Response
from rest_framework.views import APIView 
from .serializers import  CaisseSerializer,PanierSerializer,OrderSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
import datetime

#Fonction qui réccupère et stocke les produit à partir et vers la base des données
@api_view(['GET','POST'])
def show_list(request):
    if(request.method=="GET"):
        r1= caisse.objects.all()#Récupperer tout les objet de la table Caisse de la base des données
        r2= CaisseSerializer(r1, many=True)#Sérialisations des données
        return Response (r2.data) 
    
    elif (request.method=="POST"):
        serializers= CaisseSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)#Réponse JSON
    
#Fonction qui réccupère et stocke les produit du client à partir et vers la base des données
@api_view(['GET','POST'])
def show_list_panier(request):
    if(request.method=="GET"):
        r1= panier.objects.all()
        r2= PanierSerializer(r1, many=True)
        return Response (r2.data) 
    
    elif (request.method=="POST"):
        serializers= PanierSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Fonction qui affiche la ticket de caisse et stocke les produit acheter à partir et vers la base des données
@api_view(['GET','POST'])
def detail_ticket(request):
    if(request.method=="GET"):
        r1= order.objects.all()
        r2= OrderSerializer(r1, many=True)
        return Response (r2.data) 
    
    elif (request.method=="POST"):
        serializers= OrderSerializer(data=request.data)
        if (serializers.is_valid()):
            serializers.save()
            return Response(serializers.data, status=200)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

