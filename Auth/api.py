from rest_framework import viewsets, permissions

from . import serializers
from . import models


class StudentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Student class"""

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class AdminViewSet(viewsets.ModelViewSet):
    """ViewSet for the Admin class"""

    queryset = models.Admin.objects.all()
    serializer_class = serializers.AdminSerializer
    permission_classes = [permissions.IsAuthenticated]


class RoleViewSet(viewsets.ModelViewSet):
    """ViewSet for the Role class"""

    queryset = models.Role.objects.all()
    serializer_class = serializers.RoleSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
