from rest_framework import serializers
from product.models import productModel

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=productModel
        fields = ['pk','description', 'price', 'quantity']


        #converts to json
        #validates for data passed