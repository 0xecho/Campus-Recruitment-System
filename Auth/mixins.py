from django.contrib.auth.mixins import LoginRequiredMixin
from . import models


class StudentRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not str(request.user.role) == "Student": 
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not str(request.user.role) == "Admin": 
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CompanyRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not str(request.user.role) == "Company": 
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SystemRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not str(request.user.role) == "System": 
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

class OwnerRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):

        print(request.user,self.model.objects.get(pk=kwargs['pk']).client)

        if not request.user.is_authenticated or not request.user == self.model.objects.get(pk=kwargs['pk']).client:

            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)