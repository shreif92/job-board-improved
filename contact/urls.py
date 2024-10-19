from django.urls import path
from . import views

app_name = 'contact'  # تحديد اسم التطبيق (namespace)



urlpatterns = [
    path('', views.send_message, name='contact'),
]
