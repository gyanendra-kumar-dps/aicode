import colorama
import re,random
from colorama import Fore,init
init()
destinations = {"beaches": ["Bali", "Maldives", "Phuket"],"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],"cities": ["Tokyo", "Paris", "New York"]}
jokes = ["Why don't programmers like nature? Too many bugs!","Why did the computer go to the doctor? Because it had a virus!","Why do travelers always feel warm? Because of all their hot spots!"]
def normalize_input(txt):
    return re.sub(r"\s+", " ", str(txt).strip().lower())
def packing_det(n):
    if n!=1:
        print(f'so you are going for {n} days')
    else:
        print(f'so you are going for {n} day')
    print('i can give you tips for packing')
    print('you can take chargers/adapters')
    print('take cloths also')
    print('have a great trip!!!')
def reccomend():
    print('Tell where you want to go beaches,cities or mountains')
    inp1=input('where you want to go:')
    if inp1=='cities':
        print(f'we have {len(destinations[inp1])} option these are {destinations[inp1]}')
    elif inp1=='mountains':
         print(f'we have {len(destinations[inp1])} option these are {destinations[inp1]}')
    elif inp1=='beaches':
         print(f'we have {len(destinations[inp1])} option these are {destinations[inp1]}')
    else:
        print('repeat pls')
        reccomend()
    inp=input('which of these you choose')
    if inp in destinations[inp1]:
        print(f'{inp} oh nice choice!')
    else:
        print('its not there unfortunately')
        reccomend()
    inp2=input('how many days you are going for')
    packing_det(inp2)
def main():
    inp=input('whats your preference:')
    if 'reccomend' in inp:
        reccomend()
    elif inp=='joke':
        print('heres a joke!!!')
        print(jokes[random.randrange(0,len(jokes)-1)])
    else:
        print('i could not understand')
print(f'{Fore.BLUE}I am a travel bot')
print('i can recommend beaches mountains and jokes too!!')
while True:
    main()
    