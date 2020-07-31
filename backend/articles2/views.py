from .models import Food, Rate
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    dishes = Food.objects.all()
    return render(request, 'website/index.html', {'food': dishes})


def login(request):
    return render(request, 'website/log_in.html')


def sign_in(request):
    return render(request, 'website/register.html')


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "website/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


class MyLoginFormView(FormView):
    form_class = AuthenticationForm
    success_url = "/"
    template_name = "website/log_in.html"

    def form_valid(self, form):
        self.user = form.get_user()
        print(self.user)
        login(self.request, self.user)
        return super(MyLoginFormView, self).form_valid(form)
