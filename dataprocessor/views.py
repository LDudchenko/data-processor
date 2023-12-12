from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serilalizers import StatsSerializer
from .serilalizers import TemperatureSerializer
from .serilalizers import DustSerializer
from .serilalizers import HumiditySerializer
from .serilalizers import CO2Serializer
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

    return Response(map)

@api_view(['POST'])
def saveData(request):
    if isinstance(request.data, list):
        serializer = TemperatureSerializer(data=request.data, many=True)
    else:
        serializer = TemperatureSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(request.data, list):
        serializer = HumiditySerializer(data=request.data, many=True)
    else:
        serializer = HumiditySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if isinstance(request.data, list):
        serializer = CO2Serializer(data=request.data, many=True)
    else:
        serializer = CO2Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    if isinstance(request.data, list):
        serializer = DustSerializer(data=request.data, many=True)
    else:
        serializer = DustSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('Data is valid')
        print(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    return Response(serializer.data, status=status.HTTP_201_CREATED)
    