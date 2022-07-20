from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('dev/create', views.dev_create, name = "dev_create"), 
    path('dev/list', views.dev_list, name = "dev_list"), 
    path('dev/detail/<int:id>', views.dev_detail, name="dev_detail"),
    path('dev/update/<int:id>', views.dev_update, name="dev_update"),
    path("dev/delete/<int:id>", views.dev_delete, name="dev_delete"),
    path('idea/create', views.idea_create, name = "idea_create"), 
    path('idea/detail/<int:id>', views.idea_detail, name="idea_detail"),
    path('idea/update/<int:id>', views.idea_update, name="idea_update"),
    path("idea/delete/<int:id>", views.idea_delete, name="idea_delete"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
