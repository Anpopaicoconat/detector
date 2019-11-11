in1 = '''15
15
15
15
20
20
20
20
66
66
29
69
38
77
49
82
56
56
70
70
88
90
82
98
98
104
104
121
111
130
121
130
135
135
148
148
152
158
158
159
159

'''
list1 = in1.split('\n')
listout=[]
for i in list1:
    if i!='':
        i = int(i)
        if i < 32:#31 январь
            listout.append(str(i)+'.01')
        elif i < 60:# 28 февраль
            listout.append(str(i-31)+'.02')
        elif i < 91:# 31 март
            listout.append(str(i-31-28)+'.03')
        elif i < 121:# 30 апрель
            listout.append(str(i-31-28-31)+'.04')
        elif i < 152:#
            listout.append(str(i-31-28-31-30)+'.05')
        elif i < 182:#
            listout.append(str(i-31-28-31-30-31)+'.06')
for i in listout:
    print(i)
print(len(listout))

#######3
