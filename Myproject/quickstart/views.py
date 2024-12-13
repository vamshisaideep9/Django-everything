from django.shortcuts import render
from django.contrib.auth.models import Group
from quickstart.serializers import GroupSerializer, UserSerializer
from rest_framework import permissions, viewsets
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


# class UserviewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited
#     """

#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]



# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to viewed or edited.
#     """

#     queryset = Group.objects.all().order_by('name')
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class UsersCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]