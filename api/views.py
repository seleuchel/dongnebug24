from api.models import Locations, PushToken
from dongnebug.models import Complain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, LocationsSerializer, PushTokenSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer


class LocationsViewSet(viewsets.ModelViewSet):

#    def getComplains():
#        near_complains = []
#        user_latitude=Location.objects.filter(pk=2).values('latitude').first()['latitude']
#        user_longitude=Location.objects.filter(pk=2).values('longitude').first()['longitude']
#        complains = Complain.objects.all()
#        for complain in complains:
#            dist = distance.euclidean((float(complain.latitude), float(complain.longitude)), (float(user_latitude), float(user_longitude)),5)

#            if dist < 0.05:
#                self.near_complains.append(complain)
#        return near_complains

#    queryset = Complain.objects.filter(pk__in=getComplains())

    queryset=Locations.objects.all()
    serializer_class = LocationsSerializer

class PushTokenViewSet(viewsets.ModelViewSet):
    queryset = PushToken.objects.all()
    serializer_class = PushTokenSerializer