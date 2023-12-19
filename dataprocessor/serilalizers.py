from rest_framework import serializers
from base.models import StatsModel
from base.models import TemperatureModel
from base.models import HumidityModel
from base.models import CO2Model
from base.models import DustModel
from base.models import DustFields


class DustNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DustFields
        fields = '__all__'


class DustSerializer(serializers.ModelSerializer):
    class Meta:
        model = DustModel
        fields = ('timestamp', 'PM1', 'PM2', 'PM10')


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureModel
        fields = ('timestamp', 'temperature')


class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = '__all__'


class CO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Model
        fields = ['CO2', 'timestamp']


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityModel
        fields = ['humidity', 'timestamp']
