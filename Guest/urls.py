from django.urls import path,include
from Guest import views
app_name="webguest"
urlpatterns = [
    path('User/',views.User,name="User"),
    path('Login/',views.Login,name="Login"),
    path('',views.index,name="Index"),
    path('ajaxplace/',views.AjaxPlace,name="Ajaxplace"),
    path('Servicecenter/',views.Servicecenter,name="Servicecenter"),
   ]
