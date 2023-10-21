from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Business
from .serializers import BusinessSerializer

class BusinessCreateView(generics.CreateAPIView):
    """
    Create a new business instance.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessUpdateView(generics.UpdateAPIView):
    """
    Update a business instance by ID.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessDeleteView(generics.DestroyAPIView):
    """
    Delete a business instance by ID.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessListView(generics.ListAPIView):
    """
    Retrieve all business instances.
    """
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessByIDView(APIView):
    """
    Retrieve a business instance by ID.
    """
    def get_object(self, id):
        try:
            return Business.objects.get(id=id)
        except Business.DoesNotExist:
            raise Http404

    def get(self, request, id):
        business = self.get_object(id)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)

class BusinessByNameView(APIView):
    """
    Retrieve a business instance by name.
    """
    def get_object(self, name):
        try:
            return Business.objects.get(name=name)
        except Business.DoesNotExist:
            raise Http404

    def get(self, request, name):
        business = self.get_object(name)
        serializer = BusinessSerializer(business)
        return Response(serializer.data)