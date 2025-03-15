
from django.contrib import admin
from django.urls import path
from app.views import home
from app.views import search_similar

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("searchsimilar/<str:sterm>", search_similar)
]
