from django.urls import path
from . import views

app_name = 'index'  # تحديد اسم التطبيق (namespace)



urlpatterns = [
    path('', views.index, name='index'),
]
