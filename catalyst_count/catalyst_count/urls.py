
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    #including below all app's urls
    path('accounts/', include('authentication.urls')),
    path('', include('uploader.urls')),
    path('', include('count_api.urls')),
    path('', include('query_builder.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #adding media url
