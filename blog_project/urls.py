from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for create/edit blog posts'

schema_view = get_schema_view(
   openapi.Info(
      title=API_TITLE,
      default_version='v1',
      description=API_DESCRIPTION,
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Main auth
    path('api/v1/dj-rest-auth/',
         include('dj_rest_auth.urls')),  # Experimental auth
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schemaswagger-ui'),

]
