def get_radius(prompt):
    r = int(input(prompt))
    return r
def get_circle_area(r):
    area = r*r*3.14
    return area

result_r = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
result_area = get_circle_area(result_r)
print("반지름 ", result_r, '인 원의 넓이 = ','3.14 x ', result_r, ' x ', result_r,
' = ', result_area, sep='')
