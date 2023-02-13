from django.urls import path

from . import views

app_name = 'care'

urlpatterns = [
    path('', views.CareListView.as_view(), name='care_index'),  # care_list의 기본 & 목록
    path('<int:pk>/', views.CareDetailView.as_view(), name='care_detail'),
    path('<int:care_id>/reviews/', views.ReviewListView.as_view(), name='review_list'),
    path('<int:care_id>/reviews/add/', views.ReviewCreateView.as_view(), name='review_create'),
    # path('<int:care_id>/reviews/update/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('care/<int:care_id>/reviews/<int:pk>/update/', views.ReviewUpdateView.as_view(), name='review_update'),

    path('<int:care_id>/reviews/delete/', views.ReviewDeleteView.as_view(), name='review_delete'),
]

