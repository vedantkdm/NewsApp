from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect

import requests

from news_api.forms import CommentForm
from news_api.models import Post

API_KEY = 'bc605488aa764bc6a5885fa14941b5e0'


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'news_api/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'news_api/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)

def home(request):
        country = request.GET.get('country')
        category = request.GET.get('category')

        if country:
            url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
        else:
            url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']

        context = {
            'articles': articles
        }

        return render(request, 'news_api/home.html', context)


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'news_api/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'news_api/post_details.html', {'post': post, 'form': form})