from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def create_list_books(request: Request):
	if request.method == 'GET':
		books = Book.objects.order_by('title').all()
		book_serializer = BookSerializer(books, many=True)
		return Response(book_serializer.data, status.HTTP_200_OK)
	if request.method == 'POST':
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			data = {"message": "Book Created successfully", 'data': serializer.data}
			return Response(
				data=data,
				status=status.HTTP_201_CREATED
			)
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
	return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(["GET", 'PUT', 'DELETE'])
def get_update_delete_book(request: Request, pk):
	book = get_object_or_404(Book, pk=pk)
	if request.method == "GET":
		if book:
			serializer = BookSerializer(book)
			return Response(data=serializer.data, status=status.HTTP_200_OK)

	if request.method == "PUT":
		serializer = BookSerializer(data=request.data)
		print(serializer)
		if serializer.is_valid():
			serializer.update(book, serializer.data)
			return Response({'message': f"Book id : {pk} Updated"}, status.HTTP_200_OK)
		return Response({"errors": serializer.errors}, status.HTTP_400_BAD_REQUEST)

	if request.method == "DELETE":
		book.delete()
		return Response(status.HTTP_204_NO_CONTENT)
