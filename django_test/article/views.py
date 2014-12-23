from django.shortcuts import render_to_response
from django.http import HttpResponse
from article.models import Article 

#Create your views here

def articles(request):
    language = 'en-us'
    session_language = 'en-us'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    return render_to_response('articles.html',
                             {'articles':Article.objects.all(),
                              'language' : language})

def article(request, article_id=1):
    return render_to_response('article.html',
                            {'article':Article.objects.get(id=article_id)})

def language(request, language='en-us'):
    response = HttpResponse('setting language to {}'.format(language))

    response.set_cookie('lang' , language)

    return response

