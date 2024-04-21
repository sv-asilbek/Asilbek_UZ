# views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from .models import *
from contact.form import ContactForm


def home_resume(request):
    post = AboutResume.objects.all()
    context = {'post': post}
    return render(request, 'index.html', context)


def article_detail_page(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article_id=pk).order_by('-id')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()

    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }

    return render(request, 'single.html', context)


def home_page(request):
    article_list = Article.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    proj = Projects.objects.all()
    post = About.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    blog = Blog.objects.all()
    skill = Skills.objects.all()
    award = Awards.objects.all()
    art = Service.objects.all()
    form = ContactForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm()

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'educations': education,
        'experience': experience,
        'skills': skill,
        'awards': award,
        'posts': post,
        'blog': blog,
        'arts': art,
        'form': form,
        'articles': articles,
        'tags': tags,
        'proj': proj
    }
    return render(request, 'index.html', context)


def comment_submit_view(request, pk):
    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()

    comments = Comment.objects.filter(article_id=pk).order_by('-id')

    context = {'form': form, 'comments': comments, 'article': article}
    return render(request, 'single.html', context)


def search_results(request):
    query = request.GET.get('query')
    results = Categories.objects.filter(
        title__icontains=query)  # Replace YourModel and title with appropriate field names
    return render(request, 'single.html', {'results': results, 'query': query})
