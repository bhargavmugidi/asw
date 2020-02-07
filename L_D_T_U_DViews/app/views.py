from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,DeleteView,CreateView
from .models import EmployeeModel

class ShowIndex(TemplateView):
    template_name = "index.html"

class Registration(CreateView):
    model = EmployeeModel
    template_name = "reg.html"
    fields = "__all__"
    success_url = "/all/"

class ViewAll(ListView):
    model = EmployeeModel
    template_name = "viewall.html"

class Update(UpdateView):
    model = EmployeeModel
    template_name = "update.html"
    fields = ["name","salary"]
    success_url = "/all/"


class Delete(DeleteView):
    model = EmployeeModel
    success_url = "/all/"
    template_name = "delete.html"