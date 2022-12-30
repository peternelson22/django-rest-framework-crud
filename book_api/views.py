from rest_framework.views import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .serializer import BookSerializer
from .models import Book


################ FUNCTION BASE VIEWS #################

# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book_by_pk = Book.objects.get(id=pk)
#     except:
#         return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BookSerializer(book_by_pk)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#         serializer = BookSerializer(book_by_pk, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
#     if request.method == 'DELETE':
#         book_by_pk.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


################ CLASS BASE VIEWS #################


class BookList(APIView):
    def get(self, request):
      books = Book.objects.all()
      serializer = BookSerializer(books, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookSingle(APIView):

    def get_book_by_pk(self, pk):
        try:
           return Book.objects.get(id=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book_by_pk = self.get_book_by_pk(pk)
        serializer = BookSerializer(book_by_pk)
        return Response(serializer.data)

    def put(self, request, pk):
        book_by_pk = self.get_book_by_pk(pk)
        serializer = BookSerializer(book_by_pk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book_by_pk = self.get_book_by_pk(pk)
        book_by_pk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
