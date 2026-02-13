from django.urls import path,include
from .import views
from .views import *
from .views import customer_api , customer_detail_api , product_api , product_details_api 
ProductDetailsListCreateAPI,
ProductDetailsRetrieveUpdateDeleteAPI


from rest_framework.routers import DefaultRouter
from.views import ProductDetailsViewSet

router=DefaultRouter()
router.register('viewset-product-details', ProductDetailsViewSet, basename='product-details')

urlpatterns = [
    path("", views.home, name='homepage'),
    path("secondpage/", views.secondpage, name='secondpage'),
    path("Main/", views.Main, name='Maintemplate'),
    path("Categeories", views.category_list, name='Categeory'),
    path('product_details/<int:id>',views.product_id,name='product_details'),
    
    path('categories/', views.get_categeories),
    path('categories/<int:id>/', views.get_categeory),

    path('categories/create/', views.create_category),
    path('categories/update/<int:id>/', views.update_category),
    path('categories/partial-update/<int:id>/', views.partial_update_category),
    path('categories/delete/<int:id>/', views.delete_category),


     path('customers/', customer_api),
    path('customers/<int:id>/', customer_api),

    path('customer-details/', customer_detail_api),
    path('customer-details/<int:id>/', customer_detail_api),

    path('products/', product_api),
    path('products/<int:id>/', product_api),

    path('product-details/', product_details_api),
    path('product-details/<int:id>/', product_details_api),


    path('cbv/customer-details/', CustomerDetailAPI.as_view()),
    path('cbv/customer-details/<int:id>/', CustomerDetailAPI.as_view()),


    path('generic-product-details/', ProductDetailsListCreateAPI.as_view()),
    path('generic-product-details/<int:id>/', ProductDetailsRetrieveUpdateDeleteAPI.as_view()),


    path('mixin-product-details/', ProductDetailsListCreateAPI.as_view()),
    path('mixin-product-details/<int:id>/', ProductDetailsRetrieveUpdateDeleteAPI.as_view()),


    path('add/',add_number,name='add_numbers'),  #FORM CREATION URL

    path('register/',register_user,name='register'), #MODEL FORM URL
    path('success/', success_view, name='success'), #SUCCESS URL
    path('login/', views.login_view, name='login'), #PASSWORD VALIDATION URL



    path('', include(router.urls)),
]