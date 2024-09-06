from rest_framework.views import APIView
from features.api.Serializers import CategorySerializer, UserSerializer, CategoryDataSerializer, NumberPlateSerializer, TransactionSerializer
from rest_framework.response import Response
from features.models import Category, User, NumberPlate, Tansaction
from rest_framework import status

class TransactionAV(APIView):
    def get(self, request):
        try:
            transactions = Tansaction.objects.all()
            serializer = TransactionSerializer(transactions, many=True)
            print(serializer.data)
            return Response(serializer.data)
        except Tansaction.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NumberPlateAV(APIView):
    def get(self, request):
        try:
            number_plate = NumberPlate.objects.all()
            serializer = NumberPlateSerializer(number_plate, many=True)
            return Response(serializer.data)
        except NumberPlate.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = NumberPlateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryListAV(APIView):
    def get(self, request):
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
    
        except Category.DoesnotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDataAV(APIView):
    def get(self, request):
        try:
            category_data = Category.objects.all()
            serializer = CategoryDataSerializer(category_data, many=True)
            return Response(serializer.data)
        except Category.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = CategoryDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserListAV(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = CategorySerializer(users, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'status':'not found'},status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailAV(APIView):
    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    