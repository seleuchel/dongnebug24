from rest_framework.response import Response
from api.models import Locations
from dongnebug.models import Complain
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, views, generics
from api.serializers import UserSerializer, GroupSerializer, LocationsSerializer, ComplainSerializer
from django.shortcuts import get_object_or_404
from scipy.spatial import distance

from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushResponseError
from exponent_server_sdk import PushServerError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
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
            if location.token == self.request.data['token']:
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

def send_push_message(token, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        print(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'errors': exc.errors,
                'response_data': exc.response_data,
            })

    except (ConnectionError, HTTPError) as exc:
        # Encountered some Connection or HTTP error - retry a few times in
        # case it is transient.
        print({'token': token, 'message': message, 'extra': extra})


    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
    except DeviceNotRegisteredError:
        print(DeviceNotRegisteredError)
    except PushResponseError as exc:
        # Encountered some other per-notification error.
        print({
                'token': token,
                'message': message,
                'extra': extra,
                'push_response': exc.push_response._asdict(),
            })

class NearComplainViewSet(generics.ListAPIView):

    serializer_class = ComplainSerializer

    def get_queryset(self):
        near_complains = []
        # print("get_queryset() " + str(self.request.user.id))

        locations = Locations.objects.filter(author_id__exact=self.request.user.id)

        user_latitude = locations.values('latitude').first()['latitude']
        user_longitude = locations.values('longitude').first()['longitude']
        complains = Complain.objects.all().filter(is_complete=0)
        for complain in complains:
            dist = distance.euclidean((float(complain.latitude), float(complain.longitude)),
                                      (float(user_latitude), float(user_longitude)), 5)
            if dist < 0.05:
                near_complains.append(complain.id)

        location_push_token = locations.get().token
        # TODO : 푸시토큰 암호화 및 유효성 검사 할 것! :: exponent로 감싸져있는지랑, 중간에 - 있는지
        if near_complains and location_push_token:
            send_push_message(location_push_token, '내 주변에 동네북이 발견되었습니다!')
        # TODO : 사용자의 푸시 토큰으로 바꿔서 사용하기 저기 적혀있는 하드코딩된 토큰 값은 테스트용이다.
        return Complain.objects.filter(id__in=near_complains)



