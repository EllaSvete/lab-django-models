from django.urls import path

from .views import SnacksDetailView, SnacksListView

urlpatterns = [
  path('', SnacksListView.as_view(), name='snack_list'),
  path('', SnacksDetailView.as_view(), name='snack_detail')
]