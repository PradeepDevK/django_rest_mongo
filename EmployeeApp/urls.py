from django.urls import path
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentAPI),
    path('department/<int:pk>/', views.departmentDeleteAPI, name='department-delete'),
    path('employee/', views.employeeAPI),
    path('employee/<int:id>/', views.employeeAPI, name='employee-delete'),
    path('employee/saveFile/', views.SaveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
