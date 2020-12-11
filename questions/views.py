from django.shortcuts import render
from .models import Question

def start(request):
    return render(request, 'start.html')

def render_question(request):
    return render(request, 'question1.html')

def incorrect_answear(request):
    return render(request, 'next.html')

def correct_answear(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'next.html')

def score(request):
    score = Question.objects.all().count
    return render(request, 'score.html', {'score': score})

def try_again(request):
    Question.objects.all().delete()
    return render(request, 'question1.html')






