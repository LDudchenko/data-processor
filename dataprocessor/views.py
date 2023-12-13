from datetime import datetime

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
    type = request.GET.get('type')
    quantity = int(request.GET.get('quantity', 20))
    map = {}

    if type=='Temperature':
        temperaturs = TemperatureModel.objects.all().order_by('-timestamp')[:quantity]
        map = {str(obj.timestamp): obj.temperature for obj in temperaturs}
    
    if type=='Humidity':
        humidities = HumidityModel.objects.all().order_by('-timestamp')[:quantity]
        map = {str(obj.timestamp): obj.humidity for obj in humidities}

    if type=='CO2':
        co2 = CO2Model.objects.all().order_by('-timestamp')[:quantity]
        map = {str(obj.timestamp): obj.CO2 for obj in co2}

    if type=='pm1':
        pm1 = DustModel.objects.all().order_by('-timestamp')[:quantity]
        print(pm1)
        map = {str(obj.timestamp): obj.dust.PM1 for obj in pm1}
    if type=='pm2':
        pm2 = DustModel.objects.all().order_by('-timestamp')[:quantity]
        map = {str(obj.timestamp): obj.PM2 for obj in pm2}
    if type=='pm10':
        pm10 = DustModel.objects.all().order_by('-timestamp')[:quantity]
        map = {str(obj.timestamp): obj.PM10 for obj in pm10}

    return Response(map)


def checkData(request, modelSerializer):
    if isinstance(request, list):
        serializer = modelSerializer(data=request, many=True)
    else:
        serializer = modelSerializer(data=request)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
        return serializer
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def saveData(request):
    serializer_data = {}
    parseDatetime(request)
    checkData(serializer_data, TemperatureSerializer)
    checkData(serializer_data, HumiditySerializer)
    checkData(serializer_data, CO2Serializer)
    serializer_data = parseDust(request, serializer_data)
    serializer = checkData(serializer_data, DustSerializer)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


def parseDatetime(request):
    if isinstance(request.data, list):
        for json_obj in request.data:
            timestamp_obj = datetime(*map(lambda item: int(item), json_obj['timestamp'].split(', ')))
            json_obj['timestamp'] = timestamp_obj

    else:
        timestamp_obj = datetime(*map(lambda item: int(item), request.data['timestamp'].split(', ')))
        request.data['timestamp'] = timestamp_obj


def parseDust(request, serializer_data):
    if isinstance(request.data, list):
        serializer_data = list(map(lambda x: {
            'PM1': x.get('dust', {}).get('PM1', ''),
            'PM2': x.get('dust', {}).get('PM2', ''),
            'PM10': x.get('dust', {}).get('PM10', ''),
            'timestamp': x.get('timestamp', ''),
        }, request.data))
    else:
        serializer_data = {
            'PM1': request.data.get('dust', {}).get('PM1', ''),
            'PM2': request.data.get('dust', {}).get('PM2', ''),
            'PM10': request.data.get('dust', {}).get('PM10', ''),
            'timestamp': request.data.get('timestamp', ''),
        }
    return serializer_data
    