from django.views import generic
from django.contrib.auth import login
from django.shortcuts import redirect
from rest_framework import viewsets
from django.http import JsonResponse
from watson import search as watson


from . import models
from . import forms
from .mixins import *
from .serializers import *

class StudentListView(LoginRequiredMixin, generic.ListView):
    model = models.Student
    form_class = forms.StudentForm


class StudentCreateView(generic.CreateView):
    model = models.Client
    # form_class = forms.StudentSignUpForm
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
    
class UniversityListView(generic.ListView):
    model = models.University

class UniversityCreateView(AdminRequiredMixin, generic.CreateView):
    model = models.University
    form_class = forms.ClientForm

class UniversityDetailView(generic.DetailView):
    model = models.University
    form_class = forms.ClientForm

def invite(request,comp,stud):

    try:
        comp = models.Company.objects.get(pk=comp)
        stud = models.Student.objects.get(pk=stud)
        invitation = models.Invites()
        invitation.from_comp = comp
        invitation.to_stud = stud
        invitation.save()
        return JsonResponse({"message":"Invited Succesfully"})
    except Exception as e:
        # return JsonResponse({"message":"Error Inviting Student"})
        return JsonResponse(e.message)
        print(e)
        
class Notificatons(StudentRequiredMixin, generic.ListView):
    model = models.Invites
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(to_stud=self.request.user.student.id)
        return qs

class IndexPage(generic.TemplateView):

    template_name = "index.html"

    extra_context = {
        "number_of_students":len(models.Student.objects.all()),
        "number_of_companies":len(models.Company.objects.all()),
        # "number_of_openings":len(model.Student.objects.all()).
    }
    

def debug(request):
    print(123)
    print(watson.search("student"))
    return "ABDE"