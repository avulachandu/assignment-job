from rest_framework import serializers
from .models import *


class ProductDetails(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class Productioncolor(serializers.ModelSerializer):
    class Meta:
        model=Productioncolour
        fields='__all__'

class Productionimg(serializers.ModelSerializer):
    class Meta:
        model=Productionimage
        fields='__all__'