from django.shortcuts import render

from forum.models import Questions


def IndexView(request):
    latest_questions = Questions.objects.all().order_by("-date_published")[:5]
    popular_questions = Questions.objects.all().order_by("-num_replies")[:5]

    return render(request, 'core/index.html',
                  {'latest_questions': latest_questions, 'popular_questions': popular_questions
                   })
