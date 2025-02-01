from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Quiz, Question, QuizResult
from django.contrib.auth.decorators import login_required

# Create your views here.

