from rest_framework import generics
from product.models import productModel
from product.api.serializer import productSerializer
#from django.shortcuts import render,redirect

class productlistApiview(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = productSerializer

    def get_queryset(self):
        return productModel.objects.all()



class productApiview(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = productSerializer

    def get_queryset(self):
        return productModel.objects.all()
