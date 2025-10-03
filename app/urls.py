# app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/logout/", views.admin_logout_view, name="admin_logout"),
    path("admin/", admin.site.urls),

    path("login/", views.custom_login, name="login"),
    path("logout/", views.logout_get, name="logout"),  # <-- GET OK

    path("", views.dashboard, name="dashboard"),

    path("coletores/", include(("coletores.urls", "coletores"), namespace="coletores")),
    path("materiais/", include(("materiais.urls", "materiais"), namespace="materiais")),
    path("caixa/", include(("caixa.urls", "caixa"), namespace="caixa")),

    path("materiais-reciclaveis/", views.materiais_reciclaveis, name="materiais_reciclaveis"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
