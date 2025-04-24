"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include, path

admin.site.site_title = "Hydrostone Suites site admin"
admin.site.site_header = "Hydrostone Suites administration"
admin.site.index_title = "Site administration"
# https://github.com/django/django/blob/main/django/contrib/admin/sites.py


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path("secretadmin/", admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('users/', include('users.urls')),
    path("", include("tasks.urls"), name="tasks")
]
