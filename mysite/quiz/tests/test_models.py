import pytest
from quiz.models import Question, Choice

# Questionモデルのテスト
@pytest.mark.django_db
def test_question_str():
    q = Question.objects.create(question_text="question_text", explanation="explanation")
    assert str(q) == "question_text"

# Choiceモデルのテスト
@pytest.mark.django_db
def test_choice_str():
    q = Question.objects.create(question_text="question_text", explanation="explanation")
    choice = Choice.objects.create(question=q, choice_text="choice_text", is_correct=True)
    assert str(choice) == "choice_text"