from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = [
            "Phone",
            "created",
            "last_updated",
        ]

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = [
            "last_updated",
            "created",
        ]

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Admin
        fields = [
            "created",
            "last_updated",
        ]

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = [
            "id",
            "created",
            "last_updated",
        ]

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = [
            "created",
            "last_updated",
        ]
