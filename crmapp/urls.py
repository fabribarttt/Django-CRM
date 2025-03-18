from django.urls import path
from crmapp import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
    path("update_record/<int:pk>", views.update_record, name="update_record"),
]
