from rest_framework import serializers
from base.models import StatsModel
from base.models import TemperatureModel
from base.models import HumidityModel
from base.models import CO2Model
from base.models import DustModel


class DustNestedSerializer(serializers.Serializer):
     PM1=serializers.FloatField()
     PM2=serializers.FloatField(source="PM25")
     PM10=serializers.FloatField()


class DustSerializer(serializers.Serializer):
     timestamp=serializers.DateTimeField()
     dust=DustNestedSerializer(source='*')

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureModel
        fields = ['timestamp', 'temperature']

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = '__all__'

class CO2Serializer(serializers.ModelSerializer):
    class Meta:
        model = CO2Model
        fields = ['timestamp','CO2']


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityModel
        fields = ['humidity','timestamp']
