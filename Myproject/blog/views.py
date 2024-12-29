
from .models import Blog, Author, Entry
from rest_framework import generics
from .serializers import BlogSerializer, AuthorSerializer, EntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.core.cache import cache
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.


class BlogListCreate(generics.ListCreateAPIView):

    

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']
    
    @swagger_auto_schema(
        operation_description="Create and List Blogs",
        responses={200: openapi.Response('success')},
        tags=['Blogs'],
    )
   

    @method_decorator(cache_page(60*15)) # cache for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def perform_create(self, serializer):
        super().perform_create(serializer)
        cache.clear()

  

    

    




class BlogUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.clear()

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        cache.clear()


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['id']


class AuthorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class EntryListCreate(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog', 'authors']
    ordering_fields = ['pub_date']


class EntryUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]






