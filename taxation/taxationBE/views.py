from .models import UserInfo, State, Federal
from rest_framework import viewsets
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
#commit test
