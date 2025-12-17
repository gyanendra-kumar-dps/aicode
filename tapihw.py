import requests
import html
category={
    'General Knowledge':9,
    'Science & Nature':17,
    'Science: Computers':18,
    'Science: Mathematics':19,
    'Science: Gadgets':29,
    'Entertainment: Cartoon & Animations':30
}
for i,j in category.items():
    print(f'{i}:-{j}')
try:
    category=int(input('Enter a category code(18,30,19,17,29,9):'))
    difficulty=input('Enter difficulty mode(easy,medium,hard):')
    ques=int(input('Enter no of questions:'))
except:
    print('error enter a valid value')
try:
    url=f'https://opentdb.com/api.php?amount={ques}&type=multiple&difficulty={difficulty}&category={category}'
except:
    print('error enter a valid url param')
def get_data():
    try:
        data=requests.get(url)
        json_data=data.json()
        if data.status_code==200:
            return json_data['results']
    except:
        print('invalid url')
        exit(-1)
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
        if count==ques:
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
    if len(questions):
        print(f'{score//10}/{ques}')
        print(f'percentage:- {(score/10/len(questions))*100:.1f}')
    else:
        print('no of questions should be 1+')
quiz()