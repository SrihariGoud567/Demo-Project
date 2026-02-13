from django.shortcuts import render , redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Categeories
from .serializer import CategoriesSerializer
from .models import Customer, Customer_Detail, Product, ProductDetails
from .serializer import (
    CustomerSerializer,
    CustomerDetailSerializer,
    ProductSerializer,
    ProductDetailsSerializer
)

from rest_framework import generics , mixins

from rest_framework.viewsets import ModelViewSet


from .models import *

from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.pagination import CursorPagination


from.forms import *

from django import forms


# Create your views here.


def home(request):
    return HttpResponse("hello,Welcome to Django!")


def secondpage(request):
    return HttpResponse("Hii This is Second Page")

def Main(request):
    return render(request,'app1/main.html')

from .models import Categeories

def category_list(request):
    categories = Categeories.objects.all()
    return render(request, 'Products.html', {'categories': categories})



def product_id(request,id):
    qset_prod_id = ProductDetails.objects.filter(Categeories_id=id)
    return render(request, 'prod_details.html', {'produ_id': qset_prod_id})


@api_view(['GET'])
#@authentication_classes ([BasicAuthentication])
#@permission_classes ([IsAuthenticated])
def get_categeories(request):
    categories = Categeories.objects.all()
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_categeory(request, id):
    try:
        category = Categeories.objects.get(id=id)
    except Categeories.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    serializer = CategoriesSerializer(category)
    return Response(serializer.data)



@api_view(['POST'])
def create_category(request):
    serializer = CategoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_category(request, id):
    try:
        category = Categeories.objects.get(id=id)
    except Categeories.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    serializer = CategoriesSerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



@api_view(['PATCH'])
def partial_update_category(request, id):
    try:
        category = Categeories.objects.get(id=id)
    except Categeories.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    serializer = CategoriesSerializer(category, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)



@api_view(['DELETE'])
def delete_category(request, id):
    try:
        category = Categeories.objects.get(id=id)
    except Categeories.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    category.delete()
    return Response({'message': 'Deleted successfully'}, status=204)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def customer_api(request, id=None):

    if request.method == 'GET':
        if id:
            try:
                customer = Customer.objects.get(id=id)
                return Response(CustomerSerializer(customer).data)
            except Customer.DoesNotExist:
                return Response({'error': 'Not found'}, status=404)
        customers = Customer.objects.all()
        return Response(CustomerSerializer(customers, many=True).data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Customer.objects.get(id=id).delete()
        return Response(status=204)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def customer_detail_api(request, id=None):

    if request.method == 'GET':
        if id:
            detail = Customer_Detail.objects.get(id=id)
            return Response(CustomerDetailSerializer(detail).data)
        return Response(CustomerDetailSerializer(Customer_Detail.objects.all(), many=True).data)

    elif request.method == 'POST':
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        detail = Customer_Detail.objects.get(id=id)
        serializer = CustomerDetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        detail = Customer_Detail.objects.get(id=id)
        serializer = CustomerDetailSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Customer_Detail.objects.get(id=id).delete()
        return Response(status=204)
    print("FUNCTION VIEW CALLED")



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product_api(request, id=None):

    if request.method == 'GET':
        if id:
            product = Product.objects.get(id=id)
            return Response(ProductSerializer(product).data)
        return Response(ProductSerializer(Product.objects.all(), many=True).data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        Product.objects.get(id=id).delete()
        return Response(status=204)


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def product_details_api(request, id=None):

    if request.method == 'GET':
        if id:
            obj = ProductDetails.objects.get(id=id)
            return Response(ProductDetailsSerializer(obj).data)
        return Response(ProductDetailsSerializer(ProductDetails.objects.all(), many=True).data)

    elif request.method == 'POST':
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        obj = ProductDetails.objects.get(id=id)
        serializer = ProductDetailsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        obj = ProductDetails.objects.get(id=id)
        serializer = ProductDetailsSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ProductDetails.objects.get(id=id).delete()
        return Response(status=204)


#CLASS BASED API VIEWS


class CustomerDetailAPI(APIView):
    #authentication_classes=[BasicAuthentication , JWTAuthentication ,]
    #permission_classes=[IsAuthenticated]

    def get(self, request, id=None):
        if id:
            try:
                obj = Customer_Detail.objects.get(id=id)
                serializer = CustomerDetailSerializer(obj)
                return Response(serializer.data)
            except Customer_Detail.DoesNotExist:
                return Response({"error": "Not found"}, status=404)

        objs = Customer_Detail.objects.all()
        serializer = CustomerDetailSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, id):
        obj = Customer_Detail.objects.get(id=id)
        serializer = CustomerDetailSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, id):
        obj = Customer_Detail.objects.get(id=id)
        serializer = CustomerDetailSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        obj = Customer_Detail.objects.get(id=id)
        obj.delete()
        return Response({"message": "Deleted"})
    print("CLASS VIEW CALLED")



#List create Generic View For ProductDetails Model
 
class ProductDetailsListCreateAPI(generics.ListCreateAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer

# RetrieveUpdateDestroy Generic API VIEW for ProductDetails Model

class ProductDetailsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'


#List and Create (GET and POST) Mixin View for Product Details

class ProductDetailsListCreateAPI(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView):

    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

# RETRIEVE UPDATE PATCH DELETE MIXIN VIEW FOR PRODUCT DETAILS MODEL

class ProductDetailsRetrieveUpdateDeleteAPI(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView):

    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# MODEL API VIEWSET FOR PRODUCTDETAILS

class ProductDetailsViewSet(ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    pagination_class = CursorPagination
    class Meta:
        ordering = ['-created_at']   #USED FOR CURSOR PAGINATION


#BASIC FORM VIEW

def add_number(request):
    result=None
    if request.method=="POST":
        form=AddForm(request.POST)
        if form.is_valid():
            num1=form.cleaned_data['number1']
            num2=form.cleaned_data['number2']
            result=num1+num2
    else:
        form=AddForm()


    return render(request,'app1/add.html',{'form':form,'result':result})


#MODEL FORM VIEW

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save() #THIS SAVES DATA TO DATABASE
            return redirect('success') #REDIRECTS AFTER REGISTRATION
    else:
        form=UserForm()
    return render(request,'register.html',{'form':form})


# SUCCESS VIEW FOR MODEL FORM
def success_view(request):
    return render(request, 'app1/success.html')


#PASSWORD VALIDATION FOR FORMS

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check credentials
        try:
            user = User.objects.get(username=username, password=password)
            return redirect('success')
        except User.DoesNotExist:
            return render(request, 'app1/login.html', {'error': 'Invalid username or password'})

    return render(request, 'app1/login.html')

