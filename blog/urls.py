from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_blog, name="create_blog"),
    path("myblogs/", views.doctor_blogs, name="doctor_blogs"),
    path("posts/", views.patient_blog_list, name="patient_blog_list"),
    path("edit/<int:id>/", views.edit_blog, name="edit_blog"),
    path("delete/<int:id>/", views.delete_blog, name="delete_blog"),

]

