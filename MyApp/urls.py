from django.urls import path
from MyApp import views

urlpatterns = [path('adminHome/', views.adminHome, name='adminHome'),
               path('Add_category/', views.Add_category, name='Add_category'),
               path('submitCategory/', views.submitCategory, name='submitCategory'),
               path('Display_category/', views.Display_category, name='Display_category'),
               path('EditCategory/<int:dataid>/', views.EditCategory, name="EditCategory"),
               path('updateCategory/<int:dataid>/', views.updateCategory, name="updateCategory"),
               path('DeleteCategory/<int:dataid>/', views.DeleteCategory, name="DeleteCategory"),
                path('AddProduct/', views.AddProduct, name="AddProduct"),
                path('submitProduct/', views.submitProduct, name="submitProduct"),
                path('DisplayProduct/', views.DisplayProduct, name="DisplayProduct"),
                path('EditProduct/<int:dataid>/', views.EditProduct, name="EditProduct"),
                path('updateProduct/<int:dataid>/', views.updateProduct, name="updateProduct"),
                path('DeleteProduct/<int:dataid>/', views.DeleteProduct, name="DeleteProduct"),
               path('adminLogin/', views.adminLogin, name="adminLogin"),
               path('admin_login/', views.admin_login, name="admin_login"),
               path('admin_logout/', views.admin_logout, name="admin_logout"),
               ]



