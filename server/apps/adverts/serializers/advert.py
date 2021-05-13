from rest_framework.serializers import ModelSerializer

from ..models import Advert
from .category import CategorySerializer
from .city import CitySerializer


class AdvertSerializer(ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = (
            'id',
            'title',
            'description',
            'city',
            'category',
            'views',
        )
