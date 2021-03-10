from django.views.generic import ListView
from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from book.email_service import send_new_lead_email
from .models import Book, Author, Library
from .serializers import LibrarySerializer, BookSerializer, AuthorSerializer, LeadsSerializer


class BookListView(ListView):
    paginate_by = 100
    model = Book
    context_object_name = 'books'

    def get_queryset(self):
        qs = super(BookListView, self).get_queryset()
        qs.order_by('title')
        return qs


class AuthorListView(ListView):
    paginate_by = 100
    model = Author
    context_object_name = 'authors'


class LibraryListView(ListView):
    paginate_by = 10
    model = Library
    context_object_name = 'libraries'


class LibraryGetPostView(APIView):

    def get_object(self, id):
        try:
            return Library.objects.get(pk=id)
        except Library.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = LibrarySerializer(queryset)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = LibrarySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryPutView(APIView):

    def put(self, request, format=None):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibraryFilterView(APIView):

    def get(self, request, library_id, format=None):
        queryset = Book.objects.filter(libraries=library_id)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookGetPostView(APIView):

    def get_object(self, id):
        try:
            return Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = BookSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class BookPutView(APIView):

    def put(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookSearchView(APIView):

    def get(self, request, format=None):
        text = self.request.query_params.get('text', None)
        queryset = Book.objects.filter(title__contains=text)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class AuthorGetPostView(APIView):

    def get_object(self, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data)

    def post(self, request, id, format=None):
        queryset = self.get_object(id)
        serializer = AuthorSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class AuthorPutView(APIView):

    def put(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadPostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email_user = serializer.data['email']
            send_new_lead_email(email_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


book_list_view = BookListView.as_view()
author_list_view = AuthorListView.as_view()
library_list_view = LibraryListView.as_view()
