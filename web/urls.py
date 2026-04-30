"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
import web.settings as sett
from django.conf.urls.static import static

handler400 = 'apps.main.views.handler400'
handler403 = 'apps.main.views.handler403'
handler404 = 'apps.main.views.handler404'
handler500 = 'apps.main.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.main.urls',namespace='main')),
     path('ckeditor',include('ckeditor_uploader.urls')),
    path('',include('apps.company.urls',namespace='company')),
    path('',include('apps.service.urls',namespace='service')),
    path('mag/',include('apps.mag.urls',namespace='mag')),
]+static(sett.MEDIA_URL,document_root = sett.MEDIA_ROOT)
