from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    """
    top page?
    スタートボタンがあって、それを押したらdetailにページ遷移
    """
    return HttpResponse("Start Button Here")

def detail(request, question_id):
    """
    4択の選択肢を表示
    """
    return HttpResponse(f"You're looking at detail of question {question_id}.")

def results(request, question_id):
    """
    クイズのScore(正解数・正解率など)を表示
    """
    return HttpResponse(f"You're looking at the results of question {question_id}")

def answer(request, question_id):
    """
    クイズの正解の表示と解説の表示
    """
    return HttpResponse(f"The Answer is {question_id}.")

def ranking(request):
    """
    クイズのスコアのランキング
    """
    return HttpResponse("Ranking Page")