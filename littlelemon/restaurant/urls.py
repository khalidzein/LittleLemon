from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('booking/', views.BookingView.as_view(), name='booking'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/', views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuView.as_view()),
]
