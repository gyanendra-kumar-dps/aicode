import requests
def get_random_facts(x):
    res=requests.get(f'https://uselessfacts.jsph.pl/{x}.json?language=en')
    status_code=res.status_code
    if status_code==200:
        data=res.json()
        return data['text']
    else:
        return f"error {status_code}"
typeof=input("Enter which fact you want(today,random):")
if typeof.lower()!='today' and typeof.lower()!='random':
    print('Please type random or today only')
    exit()
while True:
    inp=input("Press enter to get a random fact...")
    if inp=='q' or inp=='Q':
        exit()
    print(get_random_facts(typeof.lower()))
    if typeof.lower()=='today':
        print("That's it for today")
        exit()