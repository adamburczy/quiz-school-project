from django.shortcuts import render
from .models import Question

def test(request):
    return render(request, 'questions/pytania/question2.html')

def start(request):
    return render(request, 'start.html')

def render_question1(request):
    return render(request, 'questions/question1.html')

def correct_answear1(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question2.html')

def score(request):
    score = Question.objects.count()
    return render(request, 'questions/pytania/score.html', {'score': score})

def try_again(request):
    reset = Question.objects.all().delete()
    return render(request, 'questions/question1.html', {'reset': reset})


def incorrect_answear1(request):
    return render(request, 'questions/pytania/question2.html')

def incorrect_answear2(request):
    return render(request, 'questions/pytania/question3.html')

def incorrect_answear3(request):
    return render(request, 'questions/pytania/question4.html')

def incorrect_answear4(request):
    return render(request, 'questions/pytania/question5.html')

def incorrect_answear5(request):
    return render(request, 'questions/pytania/question6.html')

def incorrect_answear6(request):
    return render(request, 'questions/pytania/question7.html')

def incorrect_answear7(request):
    return render(request, 'questions/pytania/question8.html')

def incorrect_answear8(request):
    return render(request, 'questions/pytania/question9.html')

def incorrect_answear9(request):
    return render(request, 'questions/pytania/question10.html')

def incorrect_answear10(request):
    score = Question.objects.count()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/score.html', {'score': score})



def correct_answear1(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question2.html')

def correct_answear2(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question3.html')

def correct_answear3(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question4.html')

def correct_answear4(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question5.html')

def correct_answear5(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question6.html')

def correct_answear6(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question7.html')

def correct_answear7(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question8.html')

def correct_answear8(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question9.html')

def correct_answear9(request):
    Question.objects.create()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/question10.html')

def correct_answear10(request):
    Question.objects.create()
    score = Question.objects.count()
    #counter = Question.objects.all().count + 1
    return render(request, 'questions/pytania/score.html', {'score': score})







