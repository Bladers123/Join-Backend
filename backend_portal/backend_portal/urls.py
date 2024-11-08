# urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ticket/', include('tickets_app.api.urls')),
    path('api/auth/', include('authentication_app.api.urls')),
    path('api/profile/', include('profile_app.api.urls')),
    path('api-auth', include('rest_framework.urls'))    # login in header
]
