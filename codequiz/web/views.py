from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Question, QuizResult
from django.contrib.auth.decorators import login_required

# Create your views here.
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.objects.all()
    if request.method == "POST":
        score = 0
        for question in questions:
            user_answer = int(request.POST.get(f"question_{question.id}"))
            if user_answer == question.correct_option:
                score += 1
        result = QuizResult.objects.create(user=request.user, quiz=quiz, score=score)
        return render(request, 'quiz_result.html',{'result':result})
    return render(request,'quiz_detail.html',{'quiz':quiz, 'questions':questions})

def rankings(request):
    results = QuizResult.object.all()
    return render(request,'rankings.html', {'results':results})