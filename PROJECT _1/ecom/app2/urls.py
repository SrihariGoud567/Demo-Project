from django.urls import path
from.import views

urlpatterns = [
    path("", views.hi, name='app2'),
    path("hello/", views.hello, name='app2_hello')
]
