from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include ('hello.urls')),
    path('tasks/', include ('tasks.urls')),
    path('ny/', include ('newyear.urls')),
]
