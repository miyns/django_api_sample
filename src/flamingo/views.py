from rest_framework import viewsets, routers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from flamingo.models import Information, Service
from flamingo.serializers import InformationSerializer, ServiceSerializer, ServiceDetailSerializer


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    def list(self, request):
        if request.user.is_authenticated:
            return Response({
                "username": request.user.username,
                "is_staff": request.user.is_staff,
            })
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)


class InformationViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Information.objects.all()
    serializer_class = InformationSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Service.objects.none()
    lookup_field = 'code'

    def get_serializer_class(self):
        if self.action in ("retrieve",):
            return ServiceDetailSerializer
        return ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        if not self.request.user.is_authenticated:
            queryset = queryset.filter(is_freemium=True)
        return queryset


api_router = routers.SimpleRouter()
api_router.register(r'auth', AuthViewSet, 'auth')
api_router.register(r'information', InformationViewSet, 'information')
api_router.register(r'services', ServiceViewSet, 'service')
