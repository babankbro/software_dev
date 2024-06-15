from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet2, name="greet"),
    #path("sarayut", views.sarayut, name="sarayut"),
    #path("david", views.david, name="david")
] 