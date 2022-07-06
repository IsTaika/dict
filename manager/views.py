from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views import generic
from .models import Dict as Dict_Model, Category as Category_Model


# Create your views here.


def index(request):
    return render(
        request, 'index.html'
    )


class registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'


class words(LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    model = Dict_Model
    template_name = 'words.html'

    def get_queryset(self):
        return Dict_Model.objects.filter(executor = self.request.user)


class categories(LoginRequiredMixin, generic.ListView):
    model = Category_Model
    login_url = reverse_lazy('login')
    template_name = 'categories.html'
    def get_queryset(self):
        return Category_Model.objects.filter(owner = self.request.user)


class categories_detail(LoginRequiredMixin, generic.DetailView):
    login_url = reverse_lazy('login')
    model = Dict_Model
    template_name = 'categories_detail.html'
