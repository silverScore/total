from django.urls import path

from . import views

app_name = 'care'

urlpatterns = [
    path('', views.CareListView.as_view(), name='care_index'),  # care_list의 기본
    # path(r'^search/$', views.CareSearchView.as_view(), name='care_search'),  # care_list에서 filter시
    path('<int:pk>/', views.CareDetailView.as_view(), name='care_detail'),
]