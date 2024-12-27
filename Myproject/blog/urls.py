from django.urls import path
from blog import views

urlpatterns = [
     
    path('v1/Blog/', views.BlogListCreate.as_view()),
    path('v1/Blog/<int:pk>/', views.BlogUpdateDelete.as_view())
]
