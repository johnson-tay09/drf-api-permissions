from django.urls import path

from .views import EntryList, EntryDetail

urlpatterns = [
    path("<int:pk>/", EntryDetail.as_view()),
    path("", EntryList.as_view()),
]