import requests
import os

API_KEY = os.environ.get('API_KEY')

def make_api_request(search_query, endpoint, language=None, sortBy=None, country=None, category=None):
    if endpoint == 'everything':
        url = f'https://newsapi.org/v2/everything?q={search_query}&language={language}&sortBy={sortBy}&apiKey={API_KEY}'
    else:
        url = f'https://newsapi.org/v2/top-headlines?q={search_query}&country={country}&category={category}&apiKey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    status = data['status']

    if status == 'ok':
        articles = data['articles']
        total_results = data['totalResults']
        for article in articles:
            print(article['title'])
        print(f'Total Results: {total_results}')
    else:
        message = data['message']
        print(f'Error: {message}')


if __name__ == '__main__':
    import sys

    # Retrieve inputs from command line arguments
    search_query = sys.argv[1]
    endpoint = sys.argv[2]
    language = sys.argv[3] if len(sys.argv) >= 4 else None
    sortBy = sys.argv[4] if len(sys.argv) >= 5 else None
    country = sys.argv[5] if len(sys.argv) >= 6 else None
    category = sys.argv[6] if len(sys.argv) >= 7 else None

    make_api_request(search_query, endpoint, language, sortBy, country, category)
