from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('products/', include('products.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    # path('', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ay haga b3d eldomain b3d al /
# alhoa seif hena
# www.site.com/seif
