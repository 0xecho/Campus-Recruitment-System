import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Student_list_view():
    instance1 = test_helpers.create_Auth_Student()
    instance2 = test_helpers.create_Auth_Student()
    client = Client()
    url = reverse("Auth_Student_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Student_create_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    url = reverse("Auth_Student_create")
    data = {
        "Phone": "text",
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Student_detail_view():
    client = Client()
    instance = test_helpers.create_Auth_Student()
    url = reverse("Auth_Student_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Student_update_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    instance = test_helpers.create_Auth_Student()
    url = reverse("Auth_Student_update", args=[instance.pk, ])
    data = {
        "Phone": "text",
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Company_list_view():
    instance1 = test_helpers.create_Auth_Company()
    instance2 = test_helpers.create_Auth_Company()
    client = Client()
    url = reverse("Auth_Company_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Company_create_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    url = reverse("Auth_Company_create")
    data = {
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Company_detail_view():
    client = Client()
    instance = test_helpers.create_Auth_Company()
    url = reverse("Auth_Company_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Company_update_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    instance = test_helpers.create_Auth_Company()
    url = reverse("Auth_Company_update", args=[instance.pk, ])
    data = {
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Admin_list_view():
    instance1 = test_helpers.create_Auth_Admin()
    instance2 = test_helpers.create_Auth_Admin()
    client = Client()
    url = reverse("Auth_Admin_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Admin_create_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    url = reverse("Auth_Admin_create")
    data = {
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Admin_detail_view():
    client = Client()
    instance = test_helpers.create_Auth_Admin()
    url = reverse("Auth_Admin_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Admin_update_view():
    client = test_helpers.create_Auth_Client()
    client = Client()
    instance = test_helpers.create_Auth_Admin()
    url = reverse("Auth_Admin_update", args=[instance.pk, ])
    data = {
        "client": client.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Role_list_view():
    instance1 = test_helpers.create_Auth_Role()
    instance2 = test_helpers.create_Auth_Role()
    client = Client()
    url = reverse("Auth_Role_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Role_create_view():
    client = Client()
    url = reverse("Auth_Role_create")
    data = {
        "id": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Role_detail_view():
    client = Client()
    instance = test_helpers.create_Auth_Role()
    url = reverse("Auth_Role_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Role_update_view():
    client = Client()
    instance = test_helpers.create_Auth_Role()
    url = reverse("Auth_Role_update", args=[instance.pk, ])
    data = {
        "id": 1,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Client_list_view():
    instance1 = test_helpers.create_Auth_Client()
    instance2 = test_helpers.create_Auth_Client()
    client = Client()
    url = reverse("Auth_Client_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Client_create_view():
    role = test_helpers.create_Auth_Role()
    client = Client()
    url = reverse("Auth_Client_create")
    data = {
        "role": role.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Client_detail_view():
    client = Client()
    instance = test_helpers.create_Auth_Client()
    url = reverse("Auth_Client_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Client_update_view():
    role = test_helpers.create_Auth_Role()
    client = Client()
    instance = test_helpers.create_Auth_Client()
    url = reverse("Auth_Client_update", args=[instance.pk, ])
    data = {
        "role": role.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
