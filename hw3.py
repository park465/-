def get_sale_rate(prompt):
    global sale_rate
    sale_rate= int(input(prompt))
def get_saled_price(prompt):
    saled_price=int(input(prompt))
    return saled_price
def get_fixed_price(saled_price):
    return int(saled_price/((100-sale_rate)/100))

get_sale_rate('할인율은? ')
A= get_saled_price('A 상품의 할인된 가격은? ')
B= get_saled_price('B 상품의 할인된 가격은? ')
print('A 상품의 정가는', get_fixed_price(A), '원')
print('B 상품의 정가는', get_fixed_price(B), '원')
