from django.apps import AppConfig
from watson import search as watson
# from .models import *

class AuthConfig(AppConfig):
    name = "Auth"
    def ready(self):
        m1 = self.get_model("Student")
        m2 = self.get_model("Admin")
        m3 = self.get_model("Company")
        # m4 = self.get_model("System")
        watson.register(m1,exclude=())
        watson.register(m2,exclude=())
        watson.register(m3,exclude=())
        # watson.register(m4)

