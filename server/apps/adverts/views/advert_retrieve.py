from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from ..serializers import AdvertSerializer
from ..services import AdvertViewCountService


class AdvertRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdvertSerializer

    def retrieve(self, request: Request, *_, **__) -> Response:
        advert = self.get_object()
        serializer = self.get_serializer(advert)
        resp = Response(serializer.data)

        AdvertViewCountService.count(request, advert)
        return resp
