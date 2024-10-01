from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),    
    path('login/', views.loginPage, name="login"),    
    path('logout/', views.loginPage, name="logout"),    


    path('', views.home, name="home"),
    path('inventory/', views.inventory, name="inventory"),
    path('customers/', views.customers, name="customer"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),

]
