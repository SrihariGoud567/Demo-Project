from django.contrib import admin

# Register your models here.

from app1.models import Customer,Customer_Detail,Product,Categeories,ProductDetails

admin.site.register(Customer)
admin.site.register(Customer_Detail)
admin.site.register(Product)
admin.site.register(Categeories)
admin.site.register(ProductDetails)