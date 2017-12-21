import datetime
def nextFibo(a,b):
    return a+b

def norecursion():
    number1=1
    number2=1
    timer=datetime.datetime.now()
    for index in range(2,1000000):
        number3=number2+number1
        number1, number2 =number2, number3
    print(number3)
    print(datetime.datetime.now()-timer);

def fibo(index):
    if index<0:
        return
    if index==1 or index==0:
        return 1
    else:
        return fibo(index-1)+fibo(index-2)

def recursive(current_index,max_index,sum):
    if current_index<3:
        sum+=1;
    else:
        return recursive(current_index+1,max_index,sum)

def f(last,current,index,max,sum):
    index= index +1
    if index>max:
        return current
    else:
        aux=current
        current=last+current
        last=aux
        sum= sum+current
        return f(last,current,index,max,sum)


#print(fibo(9))
timer=datetime.datetime.now()
print(f(1,1,0,1000,0))
print(datetime.datetime.now()-timer)