from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    """
    top page?
    スタートボタンがあって、それを押したらdetailにページ遷移
    """
    if request.method == "POST":
        request.session["current_question_index"] = 0
        request.session["score"] = 0
        return redirect("quiz:detail")
    return render(request, "quiz/index.html")

def detail(request):
    """
    4択の選択肢を表示
    """
    index = request.session.get("current_question_index", 0)
    questions = list(Question.objects.all())

    if index >= len(questions):
        return redirect("quiz:results")
    
    question = questions[index]
    return render(request, "quiz/detail.html", {"question": question})

def answer(request):
    if request.method != "POST":
        return redirect("quiz.detail")
    
    index = request.session.get("current_question_index", 0) # TODO: この第二引数の0何？
    questions = list(Question.objects.all())
    question = questions[index]
    selected_choice = question.choice_set.get(pk=request.POST["choice"])

    is_correct = selected_choice.is_correct
    if is_correct:
        request.session["score"] += 1
    
    request.session["current_question_index"] += 1
    correct_choices = Choice.objects.filter(question=question, is_correct=True).first()

    exist_next_question = index + 1 < len(questions)

    return render(request, "quiz/answer.html", {
        "question": question,
        "is_correct": is_correct,
        "correct_choices": correct_choices,
        "explanation": question.explanation,
        "selected_choice": selected_choice,
        "exist_next_question": exist_next_question
    })


def results(request):
    """
    クイズのScore(正解数・正解率など)を表示
    """
    score = request.session.get("score", 0)
    total = Question.objects.count()
    return render(request, "quiz/results.html", {
        "score": score,
        "total": total,
        "percent": int(score / total * 100 ) if total > 0 else 0
    })

def ranking(request):
    """
    クイズのスコアのランキング
    """
    return HttpResponse("Ranking Page")