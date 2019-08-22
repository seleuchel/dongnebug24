from rest_framework.response import Response
from api.models import Locations
from dongnebug.models import Complain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, generics
from api.serializers import UserSerializer, GroupSerializer, LocationsSerializer, ComplainSerializer
from django.shortcuts import get_object_or_404
from scipy.spatial import distance
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

    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

    def create(self, request, *args, **kwargs):
        self.lookup_field = 'token'
        locations = list(Locations.objects.all())

        def get_object():
            obj = get_object_or_404(Locations, token=self.request.data['token'])
            return obj

        for location in locations:
            if location.token == self.request.data['token' ]:
                # update 넣기

                instance = get_object()
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                self.perform_update(serializer)

                if getattr(instance, '_prefetched_objects_cache', None):
                    # If 'prefetch_related' has been applied to a queryset, we need to
                    # forcibly invalidate the prefetch cache on the instance.
                    instance._prefetched_objects_cache = {}

                return Response(serializer.data)
            return Response()


class NearComplainViewSet(generics.ListAPIView):

    serializer_class = ComplainSerializer

    def get_queryset(self):
        near_complains = []
        # print("get_queryset() " + str(self.request.user.id))
        locations = Locations.objects.filter(author_id__exact=self.request.user.id)
        user_latitude = locations.values('latitude').first()['latitude']
        user_longitude = locations.values('longitude').first()['longitude']
        complains = Complain.objects.all()
        for complain in complains:
            dist = distance.euclidean((float(complain.latitude), float(complain.longitude)),
                                      (float(user_latitude), float(user_longitude)), 5)
            if dist < 0.05:
                near_complains.append(complain.id)
        return Complain.objects.filter(id__in=near_complains)

    # def get_object(self, pk):
    #     near_complains = []
    #     print("get_object" + str(pk))
    #     locations = Locations.objects.filter(author_id__exact=self.request.user.id)
    #     user_latitude = locations.values('latitude').first()['latitude']
    #     user_longitude = locations.values('longitude').first()['longitude']
    #     complains = Complain.objects.all()
    #     for complain in complains:
    #         dist = distance.euclidean((float(complain.latitude), float(complain.longitude)),
    #                                   (float(user_latitude), float(user_longitude)), 5)
    #         if dist < 0.05:
    #             self.near_complains.append(complain)
    #         return near_complains
    #
    # def list(self, request, pk):
    #     print(pk)
    #     complains = self.get_object(pk)
    #     serializer = ComplainSerializer(complains[0])
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = ComplainSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)




    # def get_object(self):
    #     near_complains = []
    #     locations = Locations.objects.filter(author_id__exact=self.request.user.id)
    #     user_latitude = locations.values('latitude').first()['latitude']
    #     user_longitude = locations.values('longitude').first()['longitude']
    #     complains = Complain.objects.all()
    #     for complain in complains:
    #         dist = distance.euclidean((float(complain.latitude), float(complain.longitude)),
    #                                   (float(user_latitude), float(user_longitude)), 5)
    #         if dist < 0.05:
    #             self.near_complains.append(complain)
    #         return near_complains
    #
    # # queryset = get_query_set()
    #
    # def detail(self, pk):
    #     serializer = ComplainSerializer
    #     return Response(serializer.data)



# class NearByComplainsViewSet(viewsets.ModelViewSet):
#
    # def getComplains(self):
    #     near_complains = []
    #     locations = Locations.objects.filter(author_id__exact=self.request.id)
    #     user_latitude=locations.values('latitude').first()['latitude']
    #     user_longitude=locations.values('longitude').first()['longitude']
    #     complains = Complain.objects.all()
    #     for complain in complains:
    #         dist = distance.euclidean((float(complain.latitude), float(complain.longitude)), (float(user_latitude), float(user_longitude)),5)
    #         if dist < 0.05:
    #             self.near_complains.append(complain)
    #         return near_complains
#
#     queryset = Complain.objects.filter(pk__in=getComplains())
# #    queryset = Locations.objects.all()
#     serializer_class = NearByComplainsSerializer


