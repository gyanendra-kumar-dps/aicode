import requests
import html
url='https://opentdb.com/api.php?amount=5&type=multiple&category=9'
def get_data():
    data=requests.get(url)
    json_data=data.json()
    if data.status_code==200:
        return json_data['results']
def quiz():
    data=get_data()
    options=[]
    correct=[]
    questions=[]
    for idx,i in enumerate(data):
        options.append(html.unescape(i['incorrect_answers']))
        correct.append(html.unescape(i['correct_answer']))
        options[idx].append(html.unescape(i['correct_answer']))
        questions.append(html.unescape(i['question']))
    count=0
    score=0
    while True:
        if count==5:
            break
        print(f"Question:- {questions[count]}")
        for idx,i in enumerate(options[count]):
            print(f'{idx+1}:- {html.unescape(i)}')
        inp=input('enter a option (1-4)')
        try:
            if options[count][int(inp)-1]==correct[count]:
                score+=10
                print('correct')
            else:
                print('wrong')
        except:
            pass
        count+=1
    print(f'{score//10}/5')
    print(f'percentage:- {(score/100)*100}')
quiz()