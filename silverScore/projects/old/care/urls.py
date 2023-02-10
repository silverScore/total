from django.urls import path

from . import views

app_name = 'care'

urlpatterns = [
    path('', views.CareListView.as_view(), name='care_index'),  # care_list의 기본 & 목록
    path('<int:pk>/', views.CareDetailView.as_view(), name='care_detail'),
    path('reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('care/<int:care_id>/review/add/', views.ReviewCreateView.as_view(), name='review_create'),
    path('<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('<int:pk>/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
]