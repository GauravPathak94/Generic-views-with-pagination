from django.urls import path
from . import views

urlpatterns = [
    path('List/', views.ListLand.as_view(), name="list_url"),
    path('create/', views.CreateLand.as_view(), name="create_url"),
    path('Update/<int:pk>/', views.UpdateLand.as_view(), name="update_url"),
    path('Delete/<int:pk>/', views.DeleteLand.as_view(), name="delete_url"),
    path('GenPDF/', views.GenPDF, name='pdf_url'),
    path('GenPDF/<int:pk>/', views.IndPDF, name='indpdf_url')

    

    

]