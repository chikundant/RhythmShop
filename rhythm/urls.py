from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include('home.urls')),
    path('shop/', include('shop.urls')),
    path('contact/', include('contact_us.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
