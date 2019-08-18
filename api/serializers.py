from django.contrib.auth.models import User, Group
from api.models import Locations, PushToken
from dongnebug.models import Complain
from rest_framework import serializers
# from scipy.spatial import distance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ['latitude', 'longitude']

class PushTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PushToken
        fields = ['token']
