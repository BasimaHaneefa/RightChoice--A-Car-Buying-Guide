from django.urls import path,include
from UserApp import views
app_name="webuser"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('myprofile/',views.Myprofile,name="MyProfile"),
    path('editprofile/',views.EditProfile,name="EditProfile"),
    path('changepassword/',views.ChangePassword,name="ChangePassword"),
    path('search/',views.Search,name="Search"),
    path('ajaxsearch/',views.AjaxSearch,name="ajaxsearch"),
    path('ajaxbudget/',views.ajaxbudget,name="ajaxbudget"),
    path('ViewGallery/<int:cid>',views.ViewGallery,name="viewgallery"),
    path('rating/<str:cid>',views.rating,name="rating"),
    path('ajaxrating',views.ajaxrating,name="ajaxrating"),
    path('starrating/',views.starrating,name="starrating"),
    path('complaint/',views.Complaint,name="complaint"),
    path('delcomplaint/<int:did>',views.DelComplaint,name="DeleteComplaint"),
    path('editcomplaint/<int:eid>',views.EditComplaint,name="EditComplaint"),
    path('feedback/',views.Feedback,name="feedback"),
    path('delfeedback/<int:did>',views.DelFeedback,name="DeleteFeedback"),
    path('editfeedback/<int:eid>',views.EditFeedback,name="EditFeedback"),
    path('logout/',views.logout,name="Logout"),
    path('index/',views.index,name="Index"),
    path('SearchCenter/',views.SearchCenter,name="SearchCenter"),
    path('AjaxSearchCenter/',views.AjaxSearchCenter,name="AjaxSearchCenter"),
    path('Servicerequest/<int:did>',views.Servicerequest,name="Servicerequest"),
    path('Viewmyrequest/',views.Viewmyrequest,name="Viewmyrequest"),
   ]
