from django.contrib.auth.models import User, Group
from api.models import Location
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

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    """
    TODO : 특정 시간마다, 유저의 위치 정보와 민원의 위치 정보를 비교해서
    푸시 알람 하는 코드는 저장시에 하는 것 보다,
    단순히 그냥 저장 되어 있기만 하면 하는게 좋을 듯 하다.
    세션에서 active일 때만 하면 되지 않을까?

    near_complains = []
        complains = Complain.objects.all()
        for complain in complains:
            dist = round(
                distance.euclidean(
                    (complain.latitude, complain.longitude),
                    (self.validated_data['latitude'], self.validated_data['longitude'])
                ),
                5
            )

            if dist < 0.05:
                near_complains.append(complain)
    """
    class Meta:
        model = Location
        fields = ('latitude', 'longitude')


