from django.urls import path
from quickstart import views

urlpatterns = [
    path('users/', views.UsersList.as_view()),
    path('users-create/', views.UsersCreate.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view())
]
