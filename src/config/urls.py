from django.contrib import admin
from django.urls import path
import testapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('top/', testapp.views.root),
]
