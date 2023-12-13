from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer

from .serilalizers import StatsSerializer
from .serilalizers import TemperatureSerializer
from .serilalizers import DustSerializer
from .serilalizers import HumiditySerializer
from .serilalizers import CO2Serializer
from .serilalizers import DustModel
from .serilalizers import CO2Model
from base.models import TemperatureModel
from base.models import HumidityModel

@api_view(['GET'])
def getData(request):
    # Get type of stats
    param_value = request.GET.get('type')
    map = {}

    if param_value=='Temperature':
        temperaturs = TemperatureModel.objects.all()
        map = {str(obj.timestamp): obj.temperature for obj in temperaturs}
    
    if param_value=='Humidity':
        humidities = HumidityModel.objects.all()
        map = {str(obj.timestamp): obj.humidity for obj in humidities}

    if param_value=='CO2':
        co2 = CO2Model.objects.all()
        map = {str(obj.timestamp): obj.CO2 for obj in co2}

    if param_value=='dust':
        pm1 = DustModel.objects.all()
        print(pm1)
        map = {str(obj.timestamp): obj.dust.PM1 for obj in pm1}
    if param_value=='pm2':
        pm2 = DustModel.objects.all()
        map = {str(obj.timestamp): obj.PM2 for obj in pm2}
    if param_value=='pm10':
        pm10 = DustModel.objects.all()
        map = {str(obj.timestamp): obj.PM10 for obj in pm10}

    return Response(map)


def checkData(request, modelSerializer):
    if isinstance(request.data, list):
        serializer = modelSerializer(data=request.data, many=True)
    else:
        serializer = modelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
        return serializer
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def saveData(request):
    checkData(request, TemperatureSerializer)
    checkData(request, HumiditySerializer)
    checkData(request, CO2Serializer)
    serializer = checkData(request, DustSerializer)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    