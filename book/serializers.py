from rest_framework import serializers
from .models import *


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    libraries = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Library.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'libraries')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')


class LeadsSerializer(serializers.ModelSerializer):
    library = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Library.objects.all())

    class Meta:
        model = Leads
        fields = ('id', 'email', 'fullname', 'phone', 'library')
