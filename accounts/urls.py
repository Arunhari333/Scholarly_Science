from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.index,name="index"),
    #path('register/', include('accounts.urls'))
    path("",views.register,name='register'),
    path('detail/',views.detail, name ='detail'),
]
