from django.views import generic
from django.contrib.auth import login
from django.shortcuts import redirect

from . import models
from . import forms
from .mixins import *

class StudentListView(LoginRequiredMixin, generic.ListView):
    model = models.Student
    form_class = forms.StudentForm


class StudentCreateView(generic.CreateView):
    model = models.Client
    form_class = forms.StudentSignUpForm
    template_name = "registration/signup.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = "Student"
        return super().get_context_data(**kwargs)

    def form_valid(self ,form):
        user = form.save()
        login(self.request, user)
        return redirect("index")

class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Student
    form_class = forms.StudentForm


class StudentUpdateView(OwnerRequiredMixin, generic.UpdateView):
    model = models.Student
    form_class = forms.StudentForm
    pk_url_kwarg = "pk" # TODO: Students can only view their page


class CompanyListView(LoginRequiredMixin, generic.ListView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyCreateView(AdminRequiredMixin, generic.CreateView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Company
    form_class = forms.CompanyForm


class CompanyUpdateView(AdminRequiredMixin, generic.UpdateView):
    model = models.Company
    form_class = forms.CompanyForm
    pk_url_kwarg = "pk"


class AdminListView(SystemRequiredMixin, generic.ListView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminCreateView(SystemRequiredMixin, generic.CreateView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminDetailView(SystemRequiredMixin, generic.DetailView):
    model = models.Admin
    form_class = forms.AdminForm


class AdminUpdateView(SystemRequiredMixin, generic.UpdateView):
    model = models.Admin
    form_class = forms.AdminForm
    pk_url_kwarg = "pk"


class RoleListView(SystemRequiredMixin, generic.ListView):
    model = models.Role
    form_class = forms.RoleForm

class RoleDetailView(SystemRequiredMixin, generic.DetailView):
    model = models.Role
    form_class = forms.RoleForm


class ClientListView(SystemRequiredMixin, generic.ListView):
    model = models.Client
    form_class = forms.ClientForm


class ClientCreateView(SystemRequiredMixin, generic.CreateView):
    model = models.Client
    form_class = forms.ClientForm


class ClientDetailView(SystemRequiredMixin, generic.DetailView):
    model = models.Client
    form_class = forms.ClientForm


class ClientUpdateView(SystemRequiredMixin, generic.UpdateView):
    model = models.Client
    form_class = forms.ClientForm
    pk_url_kwarg = "pk"
    

def debug(request,pk):

    print(list(request.user))
    for i in request:
        print(i)
    return "ABDE"