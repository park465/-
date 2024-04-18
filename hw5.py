def read_single_digit(n):
    if n == 0:
        return "영"
    if n == 1:
        return "일"
    if n == 2:
        return "이"
    if n == 3:
        return "삼"
    if n == 4:
        return "사"
    if n == 5:
        return "오"
    if n == 6:
        return "육"
    if n == 7:
        return "칠"
    if n == 8:
        return "팔"
    if n == 9:
        return "구"


def read_number(num):
    if 100<= num <= 999:
        a=read_single_digit(num//100)
        num= num%100
        b=read_single_digit(num//10)
        num= num%10
        c=read_single_digit(num)
        return f'{a} {b} {c}'
    elif 10<= num<= 99:
        a= read_single_digit(num//10)
        num= num%10
        b= read_single_digit(num)
        return f'{a} {b}'
    elif 0<= num<= 9:
        return read_single_digit(num)
    else:
        return -1

n=int(input("세 자리 정수 입력: "))
print(read_number(n)) 
        
        



    
