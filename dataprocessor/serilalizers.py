from rest_framework import serializers
from base.models import StatsModel
from base.models import TemperatureModel
from base.models import HumidityModel
from base.models import CO2Model
from base.models import DustModel
from base.models import DustFields


class DustNestedSerializer(serializers.Serializer):
    PM1 = serializers.FloatField()
    PM2 = serializers.FloatField()
    PM10 = serializers.FloatField()
    # class Meta:
    #     model = DustFields
    #     fields = ('PM1', 'PM2', 'PM10')


class DustSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    dust = DustNestedSerializer(source='*')

    def create(self, validated_data):
        return DustModel(timestamp=validated_data.get('timestamp'), PM1=validated_data.get('PM1'),
                         PM2=validated_data.get('PM2'), PM10=validated_data.get('PM10'))
    # dust = DustNestedSerializer()
    # class Meta:
    #     model = DustModel
    #     fields = ('timestamp', 'dust')


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
        fields = ['timestamp', 'CO2']


class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityModel
        fields = ['humidity', 'timestamp']
