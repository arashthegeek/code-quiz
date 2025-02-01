from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)  # متن سوال
    option_1 = models.CharField(max_length=255)       # گزینه 1
    option_2 = models.CharField(max_length=255)       # گزینه 2
    option_3 = models.CharField(max_length=255)       # گزینه 3
    option_4 = models.CharField(max_length=255)       # گزینه 4
    correct_option = models.IntegerField()            # شماره گزینه صحیح (1 تا 4)

    def __str__(self):
        return self.question_text

class Quiz(models.Model):
    title = models.CharField(max_length=255)         # عنوان کوییز
    description = models.TextField()                 # توضیحات کوییز
    questions = models.ManyToManyField(Question)     # سوالات کوییز (چند به چند)
    
    def __str__(self):
        return self.title

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # کاربر
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)    # کوییز
    score = models.IntegerField()                               # امتیاز کاربر در کوییز
    completion_time = models.DateTimeField(auto_now_add=True)    # زمان انجام کوییز

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - {self.score}'