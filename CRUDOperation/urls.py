from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showemp, name='showemp'),
    path('insert', views.insertemp, name='insert'),
    path('edit/<int:id>', views.editemp, name="edit"),
    path('update/<int:id>', views.updateemp, name="update"),
    path('delete/<int:id>', views.deleteemp, name="delete")
]
