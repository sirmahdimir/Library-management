from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT'])
def all_books(request: Request):
    if request.metod == 'GET':    
        books = Book.objects.order_by('title').all()
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data, status.HTTP_200_OK)
    elif request.metod == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

    return Response(None, status.HTTP_400_BAD_REQUEST) 