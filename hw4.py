def rep_char(c,n):
    print(c*n)

def draw_line_string(name):
    msg1= f'Hello {name},'
    msg2= 'Welcome to Seoul.'
    if len(msg1)>len(msg2):
        nstr=len(msg1)
    else:
        nstr=len(msg2)
    rep_char('-',nstr+2)
    print(f' {msg1} \n {msg2} ')
    rep_char('-',nstr+2)


name= input('Input his/her name: ')
draw_line_string(name)
