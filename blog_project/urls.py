from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Main auth
    path('api/v1/dj-rest-auth/',
         include('dj_rest_auth.urls')),  # Experimental auth
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='Blog API')),
    path('schema/', schema_view),

]
