from django.urls import path
from products import views

urlpatterns = [
    path("index/", views.index),
    path("about/", views.about),
    path("animal/", views.animal, name="animal"),
    path("animal/<str:animal_name>/", views.detail_animal),
    # path("delete-animal/<int:animal_id>", views.delete_animal),
    path('add-animal/', views.create_animal),
    path('edit-animal/<int:animal_id>', views.create_animal)

]


