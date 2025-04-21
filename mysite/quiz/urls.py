from django.urls import path

from . import views

app_name = "quiz"
urlpatterns = [
    # ex: /quiz/
    path("", views.index, name="index"),
    # ex: /quiz/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    path("detail/", views.detail, name="detail"),
    # ex: /quiz/5/results/
    path("results/", views.results, name="results"),
    # ex: /quiz/5/answer/
    path("answer/", views.answer, name="answer"),
    # ex: /quiz/ranking/
    path("ranking/", views.ranking, name="ranking")
]