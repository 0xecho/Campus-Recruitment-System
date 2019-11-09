from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Student(models.Model):

    #  Relationships
    client = models.OneToOneField("Auth.Client", on_delete=models.CASCADE)

    #  Fields
    Phone = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Auth_Student_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Auth_Student_update", args=(self.pk,))


class Company(models.Model):

    #  Relationships
    client = models.OneToOneField("Auth.Client", on_delete=models.CASCADE)

    #  Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Auth_Company_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Auth_Company_update", args=(self.pk,))


class Admin(models.Model):

    #  Relationships
    client = models.OneToOneField("Auth.Client", on_delete=models.CASCADE)

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Auth_Admin_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Auth_Admin_update", args=(self.pk,))


class Role(models.Model):

    #  Fields
    STUDENT = 1
    COMPANY = 2
    ADMIN = 3
    SYSTEM = 4

    ROLE_CHOICES = (
        (STUDENT,"Student"),
        (COMPANY,"Company"),
        (ADMIN,"Admin"),
        (SYSTEM,"System"),
    )
    id = models.PositiveSmallIntegerField(primary_key=True, choices=ROLE_CHOICES)

    class Meta:
        pass

    def __str__(self):
        return str(self.ROLE_CHOICES[self.pk-1][1])

    def get_absolute_url(self):
        return reverse("Auth_Role_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Auth_Role_update", args=(self.pk,))


class Client(AbstractUser):

    #  Relationships
    role = models.ForeignKey("Auth.Role",on_delete=models.CASCADE, default = 1)

    #  Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("Auth_Client_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Auth_Client_update", args=(self.pk,))
