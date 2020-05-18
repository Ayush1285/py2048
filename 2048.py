n = int(input('Enter N: '))
w = int(input('Enter W: '))
d = 0
k = 0
m = 0
flag = True
flag1 = True
import os
import copy
import random
def reverse_list():
    a = []
    for i in range(n):
        a.append(i)
    a.reverse()
    return a
def sum_a(a):
    b = reverse_list()
    for k in range(n):
        d = -1
        for j in b:
            for i in range(j+1):
                if i!=n-1 and a[k][i] == 0:
                    a[k][i]=a[k][i+1]+a[k][i]
                    a[k][i+1]=0
                elif i!=n-1 and d<i and a[k][i+1]==a[k][i]:
                    a[k][i]=a[k][i+1]+a[k][i]
                    a[k][i+1]=0
                    d=i
    return a
def sum_d(a):
    b = reverse_list()
    for k in range(n):
        d = n+1
        for j in b:
            l = []
            for x in range(n-j-1,n):
                l.append(x)
            l.reverse()
            for i in l:
                if i!=0 and a[k][i] == 0:
                    a[k][i]=a[k][i-1]+a[k][i]
                    a[k][i-1]=0
                elif i!=0 and d>i and a[k][i-1]==a[k][i]:
                    a[k][i]=a[k][i-1]+a[k][i]
                    a[k][i-1]=0
                    d=i
    return a
def sum_w(a):
    b = reverse_list()
    for k in range(n):
        d = -1
        for j in b:
            for i in range(j+1):
                if i!=n-1 and a[i][k] == 0:
                    a[i][k]=a[i+1][k]+a[i][k]
                    a[i+1][k]=0
                elif i!=n-1 and d<i and a[i+1][k]==a[i][k]:
                    a[i][k]=a[i+1][k]+a[i][k]
                    a[i+1][k]=0
                    d=i
    return a
def sum_s(a):
    b = reverse_list()
    for k in range(n):
        d = n+1
        for j in b:
            l = []
            for x in range(n-j-1,n):
                l.append(x)
            l.reverse()
            for i in l:
                if i!=0 and a[i][k] == 0:
                    a[i][k]=a[i-1][k]+a[i][k]
                    a[i-1][k]=0
                elif i!=0 and d>i and a[i-1][k]==a[i][k]:
                    a[i][k]=a[i-1][k]+a[i][k]
                    a[i-1][k]=0
                    d=i
    return a
def move_test(c):
    m = 0
    for i in range(n):
        for j in range(n):
            if c[i][j] == 0:
                m = m+1
    return m
def random2_spawn(c):
    a = random.randrange(n)
    b = random.randrange(n)
    while c[a][b] != 0:
        a = random.randrange(n)
        b = random.randrange(n)
    c[a][b] = 2
    return c
c = []
for i in range(n):
    a = []
    for j in range(n):
        a.append(0  )
    c.append(a)
c = random2_spawn(c)
os.system('cls')
for row in c:
    print(row)
while d<w:
    if flag == True:
        k = 0
        x = copy.deepcopy(c)
        c_a= copy.deepcopy(c)
        c_s= copy.deepcopy(c)
        c_d= copy.deepcopy(c)
        c_w= copy.deepcopy(c)
        c_a1 = sum_a(c_a)
        c_s1 = sum_s(c_s)
        c_d1 = sum_d(c_d)
        c_w1 = sum_w(c_w)
        m = move_test(c_a1)
        m = move_test(c_s1)+m
        m = move_test(c_d1)+m
        m = move_test(c_w1)+m
        if m == 0:
            print('Oops! You lost')
            flag = False
        else:
            b = input('Enter direction key a/s/d/w: ')
            if b == 'a':
                c = c_a    
            elif b == 's':
                c = c_s    
            elif b == 'd':
                c = c_d    
            elif b == 'w':
                c = c_w   
            else:
                print('Please enter valid key')
                continue
            for i in range(n):
                for j in range(n):
                    if c[i][j] == x[i][j]:
                        k = k+1
            if k == n**2 and m != 0:
                print('Oops! Invalid move')
                continue
            else:
                c = random2_spawn(c)
                os.system('cls')
                for row in c:
                    print(row)
                l = []
                for i in c:
                    e = max(i)
                    l.append(e)
                d = max(l)
            m = 0
    else:
        flag1 = False
        break
if flag1 == True:
    print('You Won')


            
        















































    



    
    
    
        

                
                
        







