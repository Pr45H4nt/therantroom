from django.shortcuts import render , redirect
from django.db.models import Q
from taggit.models import TaggedItem
from .models import Article , Subject
from .forms import ArticleForm , CommentForm , Feedbackform
from django.contrib.auth.decorators import login_required



@login_required(login_url='home')
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})

# Create your views here.
def homeview(request):
    query = request.GET.get('q')
    if query:
        articles = Article.objects.filter(
            Q(Title__icontains=query) | 
            Q(Content__icontains=query)
            ) 
        return render(request, 'search_results.html', {'articles': articles, 'no': len(articles)})

    else:
        articles = Article.objects.all()
        context = {
            'articles' : articles ,
            'categories' : Subject.objects.all()
        }
        return render(request, 'homepage.html', context)

def ArticleView(request, slug):
    article = Article.objects.get(Slug = slug)

    tags = article.Tags.all()
    tagged_items = TaggedItem.objects.filter(tag__in=tags)
    suggestions = Article.objects.filter(pk__in=tagged_items.values_list('object_id', flat=True)).exclude(pk=article.pk)[:3]


    context = {
        'article' : article, 
        'commentform' : CommentForm() ,
        'suggestions' : suggestions
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        print()
        if form.is_valid():
            values = form.save(commit=False)
            values.post = article
            values.save()


    return render(request, 'articlepage.html', context)

def about(request):
    return render(request, "about.html")

def donate(request):
    return render(request, "donation.html")

def feedback(request):
    form = Feedbackform()
    if request.method == 'POST':
        form =Feedbackform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "feedback.html", {'form': form})


def blowmymind(request):
    All = Article.objects.all()
    from random import choice
    article = choice(All)
    return redirect('article',slug=article.Slug)




