from django.http.request import *
from django.http.response import *
from django.shortcuts import *
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class ConsumerViewSet(ModelViewSet):
    queryset = Consumer.objects.all().order_by('id')
    serializer_class = ConsumerSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all().order_by('id')
    serializer_class = CitySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.all().order_by('id')
    serializer_class = CurrencySerializer


class LoginView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'login.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import authenticate, login
        from django.contrib.auth.models import User
        from .forms import UserForm

        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'login.html', {'form': UserForm(), 'error': True})
        user: User = authenticate(request, username=form.username, password=form.password)
        if not user:
            return render(request, 'login.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))


class RegisterView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        from .forms import UserForm
        return render(request, 'register.html', {'form': UserForm()})

    def post(self, request: HttpRequest) -> HttpResponse:
        from django.contrib.auth import login
        from .models import Consumer
        from .forms import UserForm

        form = UserForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', {'form': UserForm(), 'error': True})
        try:
            username = form.data['username']
            password = form.data['password']
            user = Consumer.objects.create_user(username, password=password)
        except:
            return render(request, 'register.html', {'form': UserForm(), 'error': True})
        login(request, user)
        return redirect(reverse('index'))


def logout(request: HttpRequest):
    from django.contrib.auth import logout
    logout(request)
    return redirect(reverse('index'))


def index(request: HttpRequest):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product(request: HttpRequest, product_id: int):
    from django.db.models import ObjectDoesNotExist
    try:
        product = Product.objects.get(pk=product_id)
    except ObjectDoesNotExist:
        return Http404()
    return render(request, 'product.html', {'product': product})
