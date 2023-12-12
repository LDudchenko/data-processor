from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serilalizers import StatsSerializer

@api_view(['GET'])
def getData(request):
    # Get type of stats
    param_value = request.GET.get('type', 'CO2')

    # Get Data from Database
    stats = {'8:20':'1.5', '8:25':'1.75', '8:30':'2.0'}
    return Response(stats)

@api_view(['POST'])
def saveData(request):
    serializer = StatsSerializer(data=request.data)
    if serializer.is_valid():
        print('Data is valid')
    #save data
    return Response(serializer.data)