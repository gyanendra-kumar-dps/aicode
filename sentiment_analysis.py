
colorama.init()
print(f'{Fore.CYAN}this is a text sentiment analysis🧐')
name=input(f'{Fore.GREEN}Whats your name:')
if name=='':
    name='bob'
print(f'{Fore.BLUE}Hi {name}')
print('Enter a sentence and you will get to know the sentiment of it')
conv_data=[]
while True:
    conv=input(f'{Fore.LIGHTMAGENTA_EX}Enter a sentence:')
    if conv!='':
        if conv=='exit':
            p=[]
            ne=[]
            n=[]
            for i in conv_data:
                    pl=TextBlob(i).polarity
                    if pl>0.25:
                        p.append(i)
                        print(f'{Fore.GREEN}polarity of {i} is positive')
                    elif pl<-0.25:
                        ne.append(i)
                        print(f'{Fore.RED}polarity of {i} is negative')
                    else:
                        n.append(i)
                        print(f'{Fore.YELLOW}polarity of {i} is neutral')
            print(f'{Fore.BLUE}Summary')
            if len(p)!=1:
                print(f'{Fore.GREEN}{len(p)} sentences are positive')
            else:
                print(f'{Fore.GREEN}{len(p)} sentence is positive')
            if len(ne)!=1:
                print(f'{Fore.RED}{len(ne)} sentences are negative')
            else:
                print(f'{Fore.RED}{len(ne)} sentence is negative')
            if len(n)!=1:
                print(f'{Fore.YELLOW}{len(n)} sentences are neutral')
            else:
                print(f'{Fore.YELLOW}{len(n)} sentence is neutral')
            break
        elif conv.lower()=='reset':
            conv_data=[]
        elif conv.lower()=='history':
            if conv_data==[]:
                print('There is no history')
            else:
                print(f'The history is {conv_data}')
                for i in conv_data:
                    pl=TextBlob(i).polarity
                    if pl>0.25:
                        print(f'{Fore.GREEN}polarity of {i} is positive')
                    elif pl<-0.25:
                        print(f'{Fore.RED}polarity of {i} is negative')
                    else:
                        print(f'{Fore.YELLOW}polarity of {i} is neutral')
        else:
            pl=TextBlob(conv).polarity
            if pl>0.25:
                print(f'{Fore.GREEN}positive')
            elif pl<-0.25:
                print(f'{Fore.RED}negative')
            else:
                print(f'{Fore.YELLOW}neutral')
            conv_data.append(conv)
    else:
        print(f'{Fore.BLUE}Enter a sentence which is not blank')
        conv=input(f'{Fore.LIGHTMAGENTA_EX}Enter a sentence:')