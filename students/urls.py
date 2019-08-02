from django.urls import path

from .views import (
    GroupListView,
    GroupDetailView,
    GroupCreateView,
    GroupUpdateView,
    GroupDeleteView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)


urlpatterns = [
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('groups/<int:id>/', GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/', GroupCreateView.as_view(), name='group_create'),
    path('groups/update/<int:id>/', GroupUpdateView.as_view(), name='group_update'),
    path('groups/delete/<int:id>/', GroupDeleteView.as_view(), name='group_delete'),
    path('student/<int:id>', StudentDetailView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:id>', StudentUpdateView.as_view(), name='student_update'),
    path('student/delete/<int:id>', StudentDeleteView.as_view(), name='student_delete'),
]
