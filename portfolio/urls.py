"""portfolio URL Configuration

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
from django.urls import path

# Omar: Import requerido para tener acceso a /media/ en éste caso a las imagenes del ejemplo
from django.conf import settings
from django.conf.urls.static import static

import jobs.views # Omar: En caso de que se importen muchas views, es mejor utilizar import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Omar: se usa para trabajar con archivos subido por usuarios
