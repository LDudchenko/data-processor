from rest_framework import serializers
from base.models import StatsModel

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsModel
        fields = '__all__'