# urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication_app.api.urls')),
    path('api/', include('profile_app.api.urls')),
    path('api-auth', include('rest_framework.urls'))    # login in header
]
