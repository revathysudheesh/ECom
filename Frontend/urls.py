from django.urls import path
from Frontend import views

urlpatterns =[ path('UserHome/', views.UserHome, name='UserHome'),
path('Contact/', views.Contact, name='Contact'),
path('ProductShop/', views.ProductShop, name='ProductShop'),
path('SingleProduct/<int:pro_id>', views.SingleProduct, name='SingleProduct'),
path('CategoryPage/<cat_name>/', views.CategoryPage, name='CategoryPage'),
path('UserRegistration/', views.UserRegistration, name='UserRegistration'),
path('saveUser/', views.saveUser, name='saveUser'),
path('user_login/', views.user_login, name="user_login"),
path('user_logout/', views.user_logout, name="user_logout"),
path('submitCart/', views.submitCart, name="submitCart"),
path('DisplayCart/', views.DisplayCart, name="DisplayCart"),
path('DeleteItem/<int:dataid>/', views.DeleteItem, name="DeleteItem"),
path('ItemCheckout/', views.ItemCheckout, name="ItemCheckout"),
path('SaveBillingAddress/', views.SaveBillingAddress, name='SaveBillingAddress')

               ]