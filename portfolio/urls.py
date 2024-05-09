from django.contrib import admin
from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index1, name='index1'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("skills", views.skills, name='skills'),
    path("contact/", views.contact, name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
