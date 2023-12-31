"""
URL configuration for cake_bake project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
import os.path

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from cake_bake import settings
from main_page.views import index
from user_page.views import private_area, private_area_order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='main'),
    path('lk/', private_area, name='lk'),
    path('lk-order/', private_area_order, name='lk-order'),
    re_path(r'^lk-order/(?P<phonenumber>((\+7)|8)\d{10})/', private_area_order, name='lk-phone'),
] + static('/frontend/', document_root=os.path.join(settings.BASE_DIR, 'frontend'))
