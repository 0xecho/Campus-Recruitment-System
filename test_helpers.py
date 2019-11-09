import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from Auth import models as Auth_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_Auth_Student(**kwargs):
    defaults = {}
    defaults["Phone"] = ""
    if "client" not in kwargs:
        defaults["client"] = create_Auth_Client()
    defaults.update(**kwargs)
    return Auth_models.Student.objects.create(**defaults)
def create_Auth_Company(**kwargs):
    defaults = {}
    if "client" not in kwargs:
        defaults["client"] = create_Auth_Client()
    defaults.update(**kwargs)
    return Auth_models.Company.objects.create(**defaults)
def create_Auth_Admin(**kwargs):
    defaults = {}
    if "client" not in kwargs:
        defaults["client"] = create_Auth_Client()
    defaults.update(**kwargs)
    return Auth_models.Admin.objects.create(**defaults)
def create_Auth_Role(**kwargs):
    defaults = {}
    defaults["id"] = ""
    defaults.update(**kwargs)
    return Auth_models.Role.objects.create(**defaults)
def create_Auth_Client(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    if "role" not in kwargs:
        defaults["role"] = create_Auth_Role()
    defaults.update(**kwargs)
    return Auth_models.Client.objects.create(**defaults)
