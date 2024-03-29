from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results
    path("<int:question_id>/", views.results, name="results"),
    # ex: polls/5/vote
    path("<int:question_id>/", views.vote, name="vote"),
    # ex /polls/owner
    path("owner", views.owner, name="owner"),
]
