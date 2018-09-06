from .models import UserInfo, State, Federal
from rest_framework import serializers


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('salary', 'marital_status', 'zip_code')

class StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = ('greater_than', 'last_bkt', 'init_tax', 'new_rate', 'state_id')

class FederalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Federal
        fields = ('greater_than', 'last_bkt', 'init_tax', 'new_rate', 'federal_id')
