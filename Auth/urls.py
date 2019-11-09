from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from django.contrib.auth.views import LoginView,LogoutView


router = routers.DefaultRouter()
router.register("Student", api.StudentViewSet)
router.register("Company", api.CompanyViewSet)
router.register("Admin", api.AdminViewSet)
router.register("Role", api.RoleViewSet)
router.register("Client", api.ClientViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("debug/", views.debug, name="debug"),
    path("Auth/Student/", views.StudentListView.as_view(), name="Auth_Student_list"),
    path("Auth/login/", LoginView.as_view(), name="login"),
    path("Auth/logout/", LogoutView.as_view(), name="logout"),
    path("Auth/Student/signup/", views.StudentCreateView.as_view(), name="Auth_Student_create"),
    path("Auth/Student/detail/<int:pk>/", views.StudentDetailView.as_view(), name="Auth_Student_detail"),
    path("Auth/Student/update/<int:pk>/", views.StudentUpdateView.as_view(), name="Auth_Student_update"),
    path("Auth/Company/", views.CompanyListView.as_view(), name="Auth_Company_list"),
    path("Auth/Company/signup/", views.CompanyCreateView.as_view(), name="Auth_Company_create"),
    path("Auth/Company/detail/<int:pk>/", views.CompanyDetailView.as_view(), name="Auth_Company_detail"),
    path("Auth/Company/update/<int:pk>/", views.CompanyUpdateView.as_view(), name="Auth_Company_update"),
    path("Auth/Admin/", views.AdminListView.as_view(), name="Auth_Admin_list"),
    path("Auth/Admin/signup/", views.AdminCreateView.as_view(), name="Auth_Admin_create"),
    path("Auth/Admin/detail/<int:pk>/", views.AdminDetailView.as_view(), name="Auth_Admin_detail"),
    path("Auth/Admin/update/<int:pk>/", views.AdminUpdateView.as_view(), name="Auth_Admin_update"),
    path("Auth/Role/", views.RoleListView.as_view(), name="Auth_Role_list"),
    path("Auth/Role/detail/<int:pk>/", views.RoleDetailView.as_view(), name="Auth_Role_detail"),
    path("Auth/Client/", views.ClientListView.as_view(), name="Auth_Client_list"),
    path("Auth/Client/signup/", views.ClientCreateView.as_view(), name="Auth_Client_create"),
    path("Auth/Client/detail/<int:pk>/", views.ClientDetailView.as_view(), name="Auth_Client_detail"),
    path("Auth/Client/update/<int:pk>/", views.ClientUpdateView.as_view(), name="Auth_Client_update"),
)
