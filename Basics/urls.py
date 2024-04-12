from django.urls import path,include
from Basics import views

urlpatterns = [
   path('Addition/',views.Sum),
   path('calculate/',views.Calculate),
   path('salary/',views.Salary),
]