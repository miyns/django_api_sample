from rest_framework import serializers
from flamingo.models import Information, Service


class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Information
        fields = ("id", "title", "contents", "published_at",)


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ("code", "name", "is_freemium",)


class ServiceDetailSerializer(serializers.ModelSerializer):

    service_status = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ("code", "name", "is_freemium", "service_status", )

    def get_service_status(self, obj):
        return "suspend"
