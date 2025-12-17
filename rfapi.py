import requests
def get_random_facts():
    res=requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    status_code=res.status_code
    if status_code==200:
        data=res.json()
        return data['text']
    else:
        return f"error {status_code}"
while True:
    inp=input("Press enter to get a random fact...")
    if inp=='q' or inp=='Q':
        exit()
    print(get_random_facts())