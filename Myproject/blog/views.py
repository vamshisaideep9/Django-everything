
from .models import Blog, Author, Entry
from rest_framework import generics
from .serializers import BlogSerializer, AuthorSerializer, EntrySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.


class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id']



class BlogUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


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






