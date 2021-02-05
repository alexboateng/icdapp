"""icdrestapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
# from .router import router

from rest_framework.urlpatterns import format_suffix_patterns
from icdmainapp import viewsets

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    path('api/icdversion', viewsets.icdverion_list),
    path('api/icdversion/<int:pk>', viewsets.icdverion_detail),
    path('api/icdcode/<int:av>', viewsets.icdcode_list),
    path('api/icdcode/<int:av>/<int:pk>', viewsets.icdcode_detail),

    path('import_data', viewsets.import_data),
    # path('api/icdcode/list/<appversion>', viewsets.ApiICDListView.as_view()),
    # path('snippets/<int:pk>', views.snippet_detail),
]
