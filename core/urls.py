from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='WelbeX',
        description='Сервис поиска ближайших машин для перевозки грузов',
        default_version='v1',
    ), 
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('docs/', schema_view.with_ui('swagger')),
]
