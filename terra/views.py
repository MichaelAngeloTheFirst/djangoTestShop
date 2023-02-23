from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse


from .models import Terrarium


class IndexView(generic.ListView):
    template_name = 'terra/index.html'
    context_object_name = 'list_of_objects'

    def get_queryset(self):
        return Terrarium.objects.all()[:5]


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('terra:login')
    template_name = 'terra/register.html'


class LoginView(LoginView):
    template_name = 'terra/login.html'


class InfoView(generic.DetailView):
    model = Terrarium
    template_name = 'terra/info.html'


class LoginRegisterView(generic.TemplateView):
    template_name = 'terra/login_register.html'


@login_required()
def buy(request, terrarium_id):
    Terrarium.objects.filter(id=terrarium_id).delete()
    return redirect('/terra/')


def logout_view(request):
    logout(request)
    return redirect('/terra/')
