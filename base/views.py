from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.conf import settings
from django.urls import reverse_lazy

from django.views import View
from django.core.mail import EmailMessage
from .forms import EmailForm

from .models import * 

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html' 
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('listen')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('listen')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('listen')
        return super(RegisterPage, self).get(*args, **kwargs)        


class KaufsListe(LoginRequiredMixin, ListView):
    model = Liste
    context_object_name = 'listen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listen'] = context['listen'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['listen'] = context['listen'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context

class ListeDetail(LoginRequiredMixin, DetailView):
    model = Liste 
    context_object_name = 'liste'
    template_name = 'base/liste.html'

class ListeErstellung(LoginRequiredMixin, CreateView):
    model = Liste
    fields = ['title', 'item1', 'preis1', 'item2', 'preis2','item3', 'preis3','item4', 'preis4','item5', 'preis5']
    success_url = reverse_lazy('listen')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListeErstellung, self).form_valid(form)  

class ListeUpdate(LoginRequiredMixin, UpdateView):
    model = Liste
    fields = ['title', 'item1', 'preis1', 'item2', 'preis2','item3', 'preis3','item4', 'preis4','item5', 'preis5']
    success_url = reverse_lazy('listen')        

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Liste
    context_object_name = 'liste'
    success_url = reverse_lazy('listen')


class TeilenView(LoginRequiredMixin, View):
    form_class = EmailForm
    template_name = 'base/teilen.html/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            betreff = form.cleaned_data['betreff']
            nachricht = form.cleaned_data['nachricht']
            email = form.cleaned_data['email']
            datei = request.FILES.getlist('datei')

            try:
                mail = EmailMessage(betreff, nachricht, settings.EMAIL_HOST_USER, [email])
                for f in datei:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'E-Mail gesendet an %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Entweder ist der Anhang zu groß oder beschädigt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Die Email kann nicht gesendet werden. Bitte versuchen Sie es später erneut'})




    

