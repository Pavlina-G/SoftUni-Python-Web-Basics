from django.urls import path

from models_django.web.views import index, delete_employee, department_details

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    # path('department/<int:pk>/', department_details, name='details department'),
    path('department/<int:pk>/<slug:slug>/', department_details, name='details department'),
    # http://127.0.0.1:8000/department/2/engineering/
)
