import requests
apikey='ND7haaOxU0AvBUTuHxRkxb2ajaIzJwQ8'
res=requests.get(f'https://api.nytimes.com/svc/movies/v2/reviews/search.json?query=godfather&api-key={apikey}')
print(res.status_code)
print(res.json())