from django.shortcuts import render
from django.contrib.auth.models import Group
from quickstart.serializers import GroupSerializer, UserSerializer, TokenSerializer
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
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from quickstart.models import UserToken


class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fileds = ['username', 'date_joined']

    @method_decorator(cache_page(60*15)) # cache for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class TokenList(generics.ListAPIView):
    queryset = UserToken.objects.all()
    serializer_class = TokenSerializer
