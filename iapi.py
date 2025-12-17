import requests
def get_jokes():
    url='https://official-joke-api.appspot.com/random_joke'
    response=requests.get(url)
    if response.status_code==200:
        json_data=response.json()
        print(f'full data:-\n{json_data}')
        print(f"Type :- {json_data['type']}")
        print(f"Joke :- {json_data['setup']} - {json_data['punchline']}")
        print(f"Id :- {json_data['id']}")
while True:
    user_input=input('Press enter for a joke or type q or exit for breaking:')
    if user_input=='q' or user_input=='exit':
        exit()
    get_jokes()