from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('image', views.ImageList.as_view(), name='image_list'),
    path('image_upload', views.image_upload, name='image_upload'),
    path('image/<int:pk>/detail', views.ShowImage.as_view(), name='image_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
