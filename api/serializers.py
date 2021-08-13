from api.services import ApiServices
from rest_framework import serializers

from .models import PackageRelease, Project


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        try:
            project = ApiServices.create_project(validated_data)
            return project
        except ValueError as error:
            raise serializers.ValidationError(error.args[0])


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True, read_only=True)
