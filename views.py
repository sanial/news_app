from django.shortcuts import render
import requests
import json
API_KEY = "de286e1b6cad442eb0f8c9ac940a48c5"


def index(request):

    #Getting the selected options
    q = request.GET.get('q')
    Endpoint = request.GET.get('Endpoint')
    sel = request.GET.get('sel')
    sel1 = request.GET.get('sel1')

    #checking whether all query parameters are present or not

    #calling the endpoints and saving the responses
    if Endpoint=='everything':
        url = f'https://newsapi.org/v2/everything?q={q}&language={sel}&sortby={sel1}&apiKey={API_KEY}'
        
    else:
        url = f'https://newsapi.org/v2/top-headlines?q={q}&country={sel}&category={sel1}&apiKey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    status = data['status']

    if status=='ok':
        articles = data['articles']
        total_results = data['totalResults']
        context = {
            'status' : status,
            'articles' : articles,
            'total_results' : total_results
        }
    else:
        message = data['message']
        context = {
            'status' : status,
            'message' : message
        }

    #rendering the results
    return render(request, 'news_app/index.html', context)
    