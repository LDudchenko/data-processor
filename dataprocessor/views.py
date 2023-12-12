from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serilalizers import StatsSerializer
from .serilalizers import TemperatureSerializer
from .serilalizers import DustSerializer

@api_view(['GET'])
def getData(request):
    # Get type of stats
    param_value = request.GET.get('type', 'CO2')

    # Get Data from Database
    stats = {'8:20':'1.5', '8:25':'1.75', '8:30':'2.0'}
    return Response(stats)

@api_view(['POST'])
def saveData(request):
    if isinstance(request.data, list):
        serializer = TemperatureSerializer(data=request.data, many=True)
    else:
        serializer = TemperatureSerializer(data=request.data)
    if serializer.is_valid():
        print('Data is valid')
        print(serializer.data)
        print(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)