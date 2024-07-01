from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.all_employees, name='all_employees'),
    path('manager/<int:manager_id>/', views.manager_hierarchy, name='manager_hierarchy'),
]
