from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status, viewsets
from django.shortcuts import get_object_or_404
from .permissions import UpdatePermission
from rest_framework.authentication import TokenAuthentication

class GetUsers(APIView):
    serializer_class = TestSerializer
    
    def get(self, request, format=None):
        return (Response({'hola': 'EMI'}))
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({'Hola': name})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):

        return (Response({'hola': 'pk'}))

class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UserProfile.objects.all()
        resp = UserSerializer(queryset, many=True)

        return Response(resp.data)
    def retrieve(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        resp = UserSerializer(user, many=False)
        return Response(resp.data)

    def destroy(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response({'message':'deleted'}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message':'created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile(viewsets.ModelViewSet):
    serializer_class = UserSerializerComplete
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdatePermission,)