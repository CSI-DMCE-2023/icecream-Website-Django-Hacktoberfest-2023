from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("contact",views.contact, name='contact'),
    path('signup',views.signupform,name='signup'),
    path('login',views.loginform,name='login'),
    path('logout',views.logout,name='logout'),
    path('comments',views.comment,name='comments'),
    path('services',views.cartit,name='services'),
    path('cartprocess',views.propayment,name='cartprocess'),
    path('delete<int:id>',views.deleteitem,name='delete'),
    path('payment',views.payment,name='payment'),
    path('successpay',views.successpay,name='successpay'),
    path('adminpage',views.admin,name='adminpage')
]
