"""titled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from titled1.settings import MEDIA_ROOT
import webapp.views


router = DefaultRouter()
router.register('users', webapp.views.UserViewSet)
router.register('consumers', webapp.views.ConsumerViewSet)
router.register('cities', webapp.views.CityViewSet)
router.register('products', webapp.views.ProductViewSet)
router.register('currencies', webapp.views.CurrencyViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webapp.views.index, name='index'),
    path('login', webapp.views.LoginView.as_view(), name='login'),
    path('register', webapp.views.RegisterView.as_view(), name='register'),
    path('api/', include(router.urls)),
    path('product/<int:product_id>', webapp.views.product, name='product'),
    re_path('^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT})
]
