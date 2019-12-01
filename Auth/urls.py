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
    path("Student/", views.StudentListView.as_view(), name="Auth_Student_list"),
    path("Student/invite/<int:comp>/<int:stud>/", views.invite, name="invite"),
    path("Student/notifications/", views.Notificatons.as_view(), name="notifications"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("Student/signup/", views.StudentCreateView.as_view(), name="Auth_Student_create"),
    path("Student/detail/<int:pk>/", views.StudentDetailView.as_view(), name="Auth_Student_detail"),
    path("Student/update/<int:pk>/", views.StudentUpdateView.as_view(), name="Auth_Student_update"),
    path("Company/", views.CompanyListView.as_view(), name="Auth_Company_list"),
    path("Company/signup/", views.CompanyCreateView.as_view(), name="Auth_Company_create"),
    path("Company/detail/<int:pk>/", views.CompanyDetailView.as_view(), name="Auth_Company_detail"),
    path("Company/update/<int:pk>/", views.CompanyUpdateView.as_view(), name="Auth_Company_update"),
    path("Admin/", views.AdminListView.as_view(), name="Auth_Admin_list"),
    path("Admin/signup/", views.AdminCreateView.as_view(), name="Auth_Admin_create"),
    path("Admin/detail/<int:pk>/", views.AdminDetailView.as_view(), name="Auth_Admin_detail"),
    path("Admin/update/<int:pk>/", views.AdminUpdateView.as_view(), name="Auth_Admin_update"),
    path("Role/", views.RoleListView.as_view(), name="Auth_Role_list"),
    path("Role/detail/<int:pk>/", views.RoleDetailView.as_view(), name="Auth_Role_detail"),
    path("University/", views.UniversityListView.as_view(), name="University_list"),
    path("University/detail/<int:pk>/", views.UniversityDetailView.as_view(), name="University_detail"),
    path("University/create/", views.UniversityCreateView.as_view(), name="University_detail"),
    path("search/", include("watson.urls", namespace="watson"))
    # path("Client/", views.ClientListView.as_view(), name="Auth_Client_list"),
    # path("Client/signup/", views.ClientCreateView.as_view(), name="Auth_Client_create"),
    # path("Client/detail/<int:pk>/", views.ClientDetailView.as_view(), name="Auth_Client_detail"),
    # path("Client/update/<int:pk>/", views.ClientUpdateView.as_view(), name="Auth_Client_update"),
)
