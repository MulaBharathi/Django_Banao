
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # ✅ important for media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('blog/', include('blog.urls')), 
]

# ✅ Serve media files (like uploaded profile pictures) in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

