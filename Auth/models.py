from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class University(models.Model):

    name = models.CharField(max_length=100)
    # logo = models.ma
    email = models.EmailField(null=True)
    location = models.CharField(max_length=100)

class Department(models.Model):

    name = models.CharField(max_length=100)
    # logo = models.ma
    email = models.EmailField(null=True)

class Student(models.Model):

    #  Relationships
    client = models.OneToOneField("Auth.Client", on_delete=models.CASCADE)

    #  Fields
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    Phone = models.CharField(max_length=15)
    email = models.EmailField(default="")
    website = models.CharField(blank=True,default="",max_length=30)
    linkedin = models.CharField(blank=True,default="",max_length=30)
    github = models.CharField(blank=True,default="",max_length=30)
    facebook = models.CharField(blank=True,default="",max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,null=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE,null=True)
    summary = models.TextField(blank=True,default="")
    # photo = mo
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

    def get_invites(self):
        return Invites.objects.filter(to_stud=self.pk)

    def invited_by(self):
        return [i.from_comp.pk for i in self.get_invites()]
    

class Company(models.Model):

    #  Relationships
    client = models.OneToOneField("Auth.Client", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(default="")
    website = models.CharField(blank=True,default="",max_length=100)
    linkedin = models.CharField(blank=True,default="",max_length=100)
    description = models.TextField(blank=True,default="")

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
    name = models.CharField(max_length=100,default="")

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

class Invites(models.Model):

    from_comp = models.ForeignKey(Company,on_delete=models.CASCADE)
    to_stud = models.ForeignKey(Student,on_delete=models.CASCADE)