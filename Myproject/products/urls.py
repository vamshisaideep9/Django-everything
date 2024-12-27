from django.urls import path, include
from products import views


urlpatterns = [
    path('create-category/', views.CreateCategory.as_view()),
    path('delete-category/<int:pk>/', views.DeleteCategory.as_view()),
    path('category-list/', views.CategoryList.as_view()),
    path('create-product/', views.CreateProduct.as_view()),
    path('delete-product/<int:pk>/', views.DeleteProduct.as_view()),
    path('product-list/', views.ListProduct.as_view())
]
