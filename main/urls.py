from . import views
from django.urls import path


urlpatterns = [
    path('instructor/', views.InstructorList.as_view()),
    path('instructor/<int:pk>/', views.InstructorDetail.as_view()),
]
