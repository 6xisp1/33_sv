#1
a=424+2*(-2)*424+2*(-2)
print(a)
#2
a=9**19
b=float(9**19)
c=int(b)
d=a-c
print(d)
#5
X=int (input())
H=int (input())
M=int (input())
print (((H*60)+X+M)//60)
print ((X+M)%60)
#6
A=int (input())
B=int (input())
H=int (input())
while A>B:
    A=int (input())
    B=int (input())
    H=int (input())
if H<A:
    print("Это недосып")
elif H>B:
    print("Пересып")
else:
    print("это нормально")
#7
year = int(input())
if (year %4==0) and (year %100 !=0) or (year %400 == 0):
    print ("Високосный")
else:
    print ("Обычный")
#8
A=float(input())
B=float(input())
C=str(input())
if c =='+':
    print(a+b)
elif c =='-':
    print(a-b)
elif c =='*':
    print(a*b)
elif c =='/' and b==0:
    print("Деление на 0!")
elif c =='/' and b!=0:
    print(a/b)
elif c =='mod' and b==0:
    print("Деление на 0!")
elif c =='mod' and b!=0:
    print(a%b)
elif c =='pow':
    print(a**b)
elif c =='div' and b==0:
    print("Деление на 0!")
elif c =='div' and b!=0:
    print(a//b)
#12
s = str(input())
sum1=int(s[0])+int(s[1])+int(s[2])
sum2=int(s[3])+int(s[4])+int(s[5])
if sum1==sum2:
    print('Счастливый')
else:
    print('Обычный')
#11
s=int(input())
n1=""
n2=""
n3=""
if s>=0:
    if s==0:
        print(str(s) + n1)
    elif s%100>=10 and s%100<=20:
        print(str(s) + n1)
    elif s%10==1:
        print(str(s) + n2)
    elif s%10==2:
        print(str(s) + n3)
    else:
        print(str(s) + n1)
