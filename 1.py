def triangle(a,b,c):
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('Right-angled Triangle')
    else:
        print("Not right angled triangle")

triangle(4,5,3)