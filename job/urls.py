from django.urls import path
from . import views

app_name = 'job'  # تحديد اسم التطبيق (namespace)



urlpatterns = [
    path('', views.job_list, name='job_list'),  # URL لعرض قائمة الوظائف
    path('add', views.add_job, name='add_job'),
    path('<slug:slug>/', views.job_details,name='job_details'),  # URL لتفاصيل الوظيفة
]
