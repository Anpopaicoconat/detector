import random
listin='''0,2
2,5
5,8
8,9
9,11
11,13
13,16
16,18
19,21
21,22
23,24
22,23
24,26
26,27
27,28
28,29
29,30

'''
list1 = listin.split('\n')
def one (list1):
    listout_t=[]
    listout_s=[]
    for i in list1:
        if i!='':
            i = int(i)
            a1=i - int(i/4)-1
            b1=i + int(i/4)+1
            a = random.choice(range(a1, i))
            b = random.choice(range(i, b1))

            t = (2*a+3*b)/5
            listout_t.append(t)
            s = ((b-a)**2)/36
            listout_s.append(s)
    for t in listout_t:
         print (t)
    print('\n\n')
    for s in listout_s:
         print (s)       

def two(list1):
    sum=0
    for i in list1:
        if i!='':
            i = float(i)
            sum+=i
    print(sum)
l=[]
for i in list1:
    if i!='':
        l.append(i)
print(l)