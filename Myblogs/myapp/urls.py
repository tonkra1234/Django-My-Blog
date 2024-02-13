from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('programming', views.programming),
    path('aviation', views.aviation),
    path('robotics', views.robotics),
    path('technology', views.technology),
    path('analytics', views.analytics),
    path('others', views.others),
    path('add_project', views.add_project),
    path('edit_project/<project_id>', views.edit_project),
    path('delete_project/<project_id>', views.delete_project),
]
