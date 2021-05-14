from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from ..serializers import AdvertSerializer
from ..services import AdvertViewCountService


class AdvertRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs):
        advert = self.get_object()
        serializer = self.get_serializer(advert)
        resp = Response(serializer.data)

        AdvertViewCountService.count(request, advert)
        return resp
