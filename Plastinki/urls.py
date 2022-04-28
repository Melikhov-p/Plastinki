from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Plastinki import settings
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('api/', include('api.urls'))
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
