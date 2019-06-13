from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from elasticsearchapp.search import search_title
from forum.models import Questions
from oauth.models import User
from .forms import CreatePost, AnswerForm


class IndexView(ListView):
    template_name = 'forum/index.html'
    context_object_name = 'latest_questions_list'
    paginate_by = 10

    def get_queryset(self):
        return Questions.objects.all().order_by("-date_published")

    # class QuestionView(DetailView):
    # template_name = 'forum/question.html'
    # model = Questions


def QuestionView(request, pk):
    question = Questions.objects.get(id=pk)

    template_name = 'forum/question.html'

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            form.instance.question_id = pk
            form.instance.user_id = request.user.id
            form.save()
            return redirect("forum:question", pk)

    else:
        form = AnswerForm()
        return render(request, template_name, {"question": question, "form": form})


def search(request):
    title = request.GET.get('q')
    results = search_title(title)

    return render(request, 'forum/search.html', {'results': results, 'q_title': title})


class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Questions
    form_class = CreatePost

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        form.save()
        return redirect("oauth:profile", username=self.request.user.username)


class UpdateQuestion(LoginRequiredMixin, UpdateView):
    model = Questions
    form_class = CreatePost
    template_name = "forum/update_question.html"

    def get_queryset(self):
        queryset = super(UpdateQuestion, self).get_queryset()
        queryset = queryset.filter(user__username=self.request.user.username)
        return queryset

    def form_valid(self, form):
        return redirect("oauth:profile", username=self.request.user.username)


class DeleteQuestion(DeleteView):
    model = Questions

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(DeleteQuestion, self).get_queryset()
        queryset = queryset.filter(user__username=self.request.user.username)
        return queryset

    def get_success_url(self):
        return reverse("oauth:profile", kwargs={"username": self.request.user.username})


def BotChat(request):
    template_name = "forum/bot.html"
    return render(request, template_name)
