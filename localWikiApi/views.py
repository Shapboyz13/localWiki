from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import wikipedia

from localWikiApi.models import Articles

# def index(request):
#     response = json.dumps([{
#         'code'        : 0,
#         'message'     : 'No Data',
#         'test'        : testing'
#     }])
#     return HttpResponse(response, content_type='text/json')

def getArticles(request, searchKeyword):
    if request.method == 'GET':
        try:
            article = Articles.objects.filter(search_keyword__contains=searchKeyword.replace(" ",''))[0]
            response = json.dumps([{
                'code'        : 1,
                'suggestions' : article.suggestions,
                'summary'     : article.summary,
            }])
        except:
            try:
                returnSummary = wikipedia.summary(searchKeyword)
                returnSuggestions = wikipedia.suggest(searchKeyword)
                response = json.dumps([{
                    'code'        : 2,
                    'summary'     : returnSummary,
                    'suggestions' : returnSuggestions,
                }])
                addArticles(searchKeyword, returnSuggestions, returnSummary)
            except wikipedia.exceptions.DisambiguationError as e:
                returnSuggestions = e.options
                response = json.dumps([{
                    'code'        : 3,
                    'suggestions' : returnSuggestions,
                }])

            except wikipedia.exceptions.PageError as e:
                response = json.dumps([{
                    'code'        : 0,
                    'message'     : 'No Data',
                }])
        if not response:
            response = json.dumps([{
                'code'        : 0,
                'message'     : 'No Data',
            }])
        return HttpResponse(response, content_type='text/json')

def addArticles(searchKeyword, returnSuggestions, returnSummary):
    article = Articles(
        search_keyword=searchKeyword,
        suggestions=returnSuggestions,
        summary=returnSummary
    )
    article.save()
