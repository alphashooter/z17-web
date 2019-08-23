from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = 'id', 'username', 'first_name', 'last_name', 'email'


class ConsumerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Consumer
        fields = 'id', 'user', 'birth_date', 'city', 'wish_list'


class CitySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ProductSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CurrencySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'
