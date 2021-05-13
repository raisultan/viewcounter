from rest_framework.generics import RetrieveAPIView

from ..serializers import AdvertSerializer


class AdvertRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdvertSerializer
