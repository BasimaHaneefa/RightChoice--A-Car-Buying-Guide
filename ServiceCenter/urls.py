from django.urls import path,include
from ServiceCenter import views
app_name="webcenter"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('myprofile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.EditProfile,name="EditProfile"),
    path('changepassword/',views.ChangePassword,name="ChangePassword"),
    path('Viewmyrequest/',views.Viewmyrequest,name="Viewmyrequest"),
    path('AcceptRequest/<int:aid>',views.AcceptRequest,name="AcceptRequest"),
    path('RejectRequest/<int:aid>',views.RejectRequest,name="RejectRequest"),
    path('logout/',views.logout,name="logout"),
      ]
