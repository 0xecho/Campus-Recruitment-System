from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        exclude =["client"]

class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.Client

    @transaction.atomic
    def save(self):
        client = super().save(commit=False)
        client.role = models.Role.objects.get(id=models.Role.STUDENT)
        client.save()
        student = models.Student.objects.create(client=client)
        # student.
        return client

class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = [
            "client",
        ]


class AdminForm(forms.ModelForm):
    class Meta:
        model = models.Admin
        fields = [
            "client",
        ]


class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = [
            "id",
        ]


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = [
            "role",
        ]
