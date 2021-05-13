from django.urls import path

from .views import AdvertListAPIView, AdvertRetrieveAPIView

urlpatterns = [
    path('advert-list/', AdvertListAPIView.as_view()),
    path('advert/<int:pk>/', AdvertRetrieveAPIView.as_view()),
]
