def input_scores(scores):
    print('[점수 입력]')
    i=1
    while True:
        score=int(input(f'#{i}? '))
        if score<0:
            break
        scores.append(score)
        i+=1
    print()
    return scores


def get_average(scores):
    return sum(scores)/len(scores)

def show_scores(scores):
    print('[점수 출력]')
    print('개인점수: ', end='')
    for i in range(len(scores)):
        print(f'{scores[i]}',end=' ')
    print()



def save_data(scores):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data():
    with open(filepath, 'rb') as file:
         return pickle.load(file) 
            
    

import pickle
import os
filepath = 'score.bin' 
if os.path.exists('score.bin'):
    print('[파일 읽기]')
    print()
    show_scores(load_data())
    print(f'평균: {get_average(load_data())}')
else:
    scores=[]
    scores=input_scores(scores)
    show_scores(scores)
    print(f'평균: {get_average(scores)}')
    save_data(scores)
