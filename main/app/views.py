from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import ProductForm


class Index(TemplateView):
    template_name = 'index.html'


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'


class About(TemplateView):
    template_name = 'about.html'


class Contacts(TemplateView):
    template_name = 'contacts.html'


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    login_url = '/login'
    success_url = '/product'
    form_class = ProductForm


class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'


class LogOut(LogoutView):
    model = User
    success_url = '/'

