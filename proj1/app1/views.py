from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from .seazializers import *
# Create your views here.
class ProductView(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class = ProductDetails
    def post (self,request):
        return self.list(request)

class ProductgView(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class = ProductDetails
    def get (self,request):
        return self.list(request)





class ProductmView(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class = Productionimg
    def post (self,request):
        return self.list(request)

class ProductcView(GenericAPIView,ListModelMixin):
    queryset=Product.objects.all()
    serializer_class = Productioncolor
    def post (self,request):
        return self.list(request)