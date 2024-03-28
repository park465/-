def exchange(money):
    won500= money//500
    result=money%500
    won100= result//100
    result%=100
    won50= result//50
    result%=50
    won10= result//10
    print('500원 동전의 개수:', won500, '\n100원 동전의 개수:', won100, '\n50원 동전의 개수:', won50, '\n10원 동전의 개수:', won10)
def get_integer(prompt):
    return int(input(prompt))


exchange(get_integer('동전으로 교환하고자 하는 금액은? '))

    

        
