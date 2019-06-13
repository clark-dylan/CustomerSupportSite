from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from .models import User
from forum.models import Questions
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'oauth/signup.html'

    # Display blank form
    def get(self, request):
        if request.user.is_authenticated():
            return redirect("oauth:profile", username=request.user)

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Store the post data
        form = self.form_class(request.POST)

        if form.is_valid():
            # Create object from form, but don't save it to the database yet
            user = form.save(commit=False)

            # Cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            login(request, user)
            return redirect("oauth:profile", username=username)

        else:
            return render(request, self.template_name, {'form': form})


class LoginView(View):
    form_class = LoginForm
    template_name = 'oauth/login.html'

    def get(self, request):
        if request.user.is_authenticated():
            return redirect("oauth:profile", username=request.user)

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Store the post data
        form = self.form_class(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect("oauth:profile", username = username)
        else:
            messages.error(request, "Error")
            return render(request, self.template_name, {'form': form})


def ProfileView(request, username):
    user = User.objects.get(username=username)

    question_list = Questions.objects.filter(user__username=username).order_by("-date_published")

    page = request.GET.get('page')
    paginator = Paginator(question_list, 10)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'oauth/profiles.html', {"user": user, "questions": questions})



