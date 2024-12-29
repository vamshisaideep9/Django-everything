"""
URL configuration for Myproject project.

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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from quickstart import views
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Django APIs",
        default_version="v1",
        description="API documentation for your project.",
        terms_of_service="https://localhost:8000/terms/",
        contact=openapi.Contact(email="vamshisaideep@gmail.com"),
        license=openapi.License(name="BSD Licenses"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('quickstart.urls')),
    path('snippet/', include('snippets.urls')),
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token-list/', views.TokenList.as_view())
]


urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
] 


"""
1) Get_schema_view: Generates a schema view for your API. It includes metadeta like
the title, version, and description of your api.

2) with_ui('swagger'): Serves swagger UI documentation.

3) with_ui('redoc): serves Redoc documentation

4) without_ui(): Generates a JSON schema for the API, useful for integrations or customizations.
"""
