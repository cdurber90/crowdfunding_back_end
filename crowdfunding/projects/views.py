from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HealthcareHero, Donation
from .serializers import DonationDetailSerializer, HealthcareHeroSerializer, DonationSerializer, HealthcareHeroDetailSerializer
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly

# --- Healthcare Hero View ---

class HealthcareHeroList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get(self, request):
        healthcarehero = HealthcareHero.objects.all()
        serializer = HealthcareHeroSerializer(healthcarehero, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HealthcareHeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
            
        return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class HealthcareHeroDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            healthcarehero = HealthcareHero.objects.get(pk=pk)
            self.check_object_permissions(self.request, healthcarehero)
            return healthcarehero
        except HealthcareHero.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        healthcarehero = self.get_object(pk)
        serializer = HealthcareHeroSerializer(healthcarehero)
        return Response(serializer.data)
    
    def put(self, request, pk):
        healthcarehero = self.get_object(pk)
        serializer = HealthcareHeroDetailSerializer(
            instance=healthcarehero,
            data=request.data,
            partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
# --- Donation view ---

class DonationList(APIView):

    def get(self, request):
        donation = Donation.objects.all()
        serializer = DonationSerializer(donation, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class DonationDetailList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def get_object(self, pk):
        try:
            donation = Donation.objects.get(pk=pk)
            self.check_object_permissions(self.request, donation)
            return donation
        except Donation.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        donation = self.get_object(pk)
        serializer = DonationDetailSerializer(donation)
        return Response(serializer.data)
    
    def put(self,request,pk):
        donation = self.get_object(pk)
        serializer = DonationDetailSerializer(
            instance=donation,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
