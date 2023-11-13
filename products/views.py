from .serializers import ProductSerializer,CategorySerializer,ProductAllSerializer
from .models import Product,Category,ProductAll
from rest_framework import viewsets


# Create your views here.
class ProductMVS(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryMVS(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 

class ProductAllMVS(viewsets.ModelViewSet):
    queryset = ProductAll.objects.all()
    serializer_class = ProductAllSerializer