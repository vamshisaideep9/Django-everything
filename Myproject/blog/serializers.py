from rest_framework import serializers
from .models import Blog, Author, Entry


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'name', 'tagline']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']

class EntrySerializer(serializers.ModelSerializer):
    blog = BlogSerializer(read_only = True)
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = ['id', 'headline', 'body_text', 'pub_date', 
                  'number_of_comments', 'number_of_pingbacks', 'rating', 'blog', 'authors']
        
