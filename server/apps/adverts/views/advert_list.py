from rest_framework.generics import ListAPIView

from ..serializers import AdvertSerializer
from ..models import Advert


class AdvertListAPIView(ListAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.select_related('city', 'category')
