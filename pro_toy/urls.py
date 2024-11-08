
from django.contrib import admin
from django.urls import path
from  app_toy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add_toy, name='add'),
    path('display/', views.display, name='display'),
    path('delete/<int:id>/', views.delete, name='delete'),

    path('update/<int:id>/', views.update, name='update'),
]
