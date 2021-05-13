from rest_framework.generics import ListAPIView

from ..serializers import AdvertSerializer


class AdvertListAPIView(ListAPIView):
    serializer_class = AdvertSerializer
