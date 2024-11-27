from django.contrib import admin
from django.urls import path
import testapp.views
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', testapp.views.root),
    path('hello/', testapp.views.hello_world),
    path('stock/', views.stock_list, name='stock_list'),
    path('stock/add/', views.stock_add, name='stock_add'),
    path('stock/edit/<int:pk>/', views.stock_edit, name='stock_edit'),
]
