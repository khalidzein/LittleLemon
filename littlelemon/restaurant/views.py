from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Booking, Menu
from django.contrib.auth.models import User
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

def index(request):
   return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [IsAuthenticated]
   
class MenuView(generics.ListCreateAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class SingleMenuView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
   queryset = Menu.objects.all()
   serializer_class = MenuSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 