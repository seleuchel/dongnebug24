from rest_framework import status
from rest_framework.response import Response
from api.models import Locations
from dongnebug.models import Complain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, LocationsSerializer
from django.shortcuts import get_object_or_404
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
                # serializer = self.get_serializer(data=request.data)
                # serializer.is_valid(raise_exception=True)
                # self.perform_create(serializer)
                # headers = self.get_success_headers(serializer.data)
                # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#
    #         # 없으면 무시
    #

    # def perform_create(self, serializer):
    #     # serializer.save()
    #     # 받은 토큰 값이 디비에 이미 있다면,
    #
    #     for key, value in self.kwargs.items():
    #         print(key, value)
    #
    #     print("-----")
    #
    #     for arg in self.args:
    #         print(arg)

        # for any in self.request.data:
        #     print(any)
        # self.request.data에 받는 모든 데이터가 들어있다.
        # for location in locations:
        #     if locations.token == self.request.data['token']:
        #         self.partial_update()



    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #





