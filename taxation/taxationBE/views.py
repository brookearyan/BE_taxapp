from .models import UserInfo, State, Federal
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserInfoSerializer, StateSerializer, FederalSerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class FederalViewSet(viewsets.ModelViewSet):
    queryset = Federal.objects.all()
    serializer_class = FederalSerializer

# @api_view(['GET', 'POST'])
#
# def UserInfoList(request):
#
#     if request.method == 'GET':
#         queryset = UserInfo.objects.all()
#         serializer = UserInfoSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserInfoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
