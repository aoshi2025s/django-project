from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    """
    top page?
    スタートボタンがあって、それを押したらdetailにページ遷移
    """
    latest_question_list = Question.objects.all()
    return render(request, "quiz/index.html", {"latest_question_list": latest_question_list})

def detail(request, question_id):
    """
    4択の選択肢を表示
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "quiz/detail.html", {"question": question})

def answer(request, question_id):
    """
    クイズの正解の表示と解説の表示
    """
    question = get_object_or_404(Question, pk=question_id)
    correct_choices = Choice.objects.filter(question=question, is_correct=True)

    # TODO:ここなに？
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
    is_correct = selected_choice.is_correct
    return render(request, "quiz/answer.html", {
        "question": question,
        "is_correct": is_correct,
        "correct_choices": correct_choices,
    })

def results(request, question_id):
    """
    クイズのScore(正解数・正解率など)を表示
    """
    return HttpResponse(f"The Answer is {question_id}.")

def ranking(request):
    """
    クイズのスコアのランキング
    """
    return HttpResponse("Ranking Page")