from django.contrib import admin
from django import forms

from . import models


class StudentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Student
        fields = "__all__"


class StudentAdmin(admin.ModelAdmin):
    form = StudentAdminForm
    list_display = [
        "client",
        "Phone",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = models.Company
        fields = "__all__"
    def save(self,commit=True):
        x = super().save(commit=False)
        # print(x.password)
        x.client.set_password(x.client.password)
        x.client.save()
        x.save()
        return x


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class AdminAdminForm(forms.ModelForm):

    class Meta:
        model = models.Admin
        fields = "__all__"


class AdminAdmin(admin.ModelAdmin):
    form = AdminAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class RoleAdminForm(forms.ModelForm):

    class Meta:
        model = models.Role
        fields = "__all__"




class RoleAdmin(admin.ModelAdmin):
    form = RoleAdminForm
    list_display = [
        "id",
    ]
    readonly_fields = [
        "id",
    ]


class ClientAdminForm(forms.ModelForm):

    class Meta:
        model = models.Client
        fields = "__all__"


class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = [
        "username",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Admin, AdminAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Department)
admin.site.register(models.University)
admin.site.register(models.Invites)
# admin.site.register(models.Client, ClientAdmin)

