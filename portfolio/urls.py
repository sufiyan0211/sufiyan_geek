from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('details/<int:pk>',views.details,name='details'),
    path('courses_details/<int:pkk>',views.courses_details,name='courses_details'),
    path('publications_details/<int:pkkk>',views.publications_details,name='publications_details'),
]


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)