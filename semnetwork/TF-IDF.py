import collections
import math
import nltk


text='''разработка информационной техники и создание новейшей технологии переработки информации на базе полученных результатов исследования информационных процессов
'''
text1='''решение научных и инженерных проблем создания, внедрения и обеспечения эффективного использования компьютерной техники и технологии во всех сферах общественной жизни.
'''
text2='''Если суждение, составляющее смысл некоторого высказывания, истинно, то и о данном высказывании говорят, что оно истинно. Сходным образом ложным называют такое высказывание, которое является выражением ложного суждения. 
'''

lst=text.lower().replace(',',' ').replace('.',' ').replace('-',' ').split()
lst1=text1.lower().replace(',',' ').replace('.',' ').replace('-',' ').split()
lst2=text2.lower().replace(',',' ').replace('.',' ').replace('-',' ').split()






def compute_tf(lst):
    tf_text=collections.Counter(lst)
    for i in tf_text:
        tf_text[i]=tf_text[i]/float(len(lst))
    return tf_text
print(compute_tf(lst))

def compute_tf1(lst1):
    tf_text=collections.Counter(lst1)

    for i in tf_text:
        tf_text[i]=tf_text[i]/float(len(lst1))
    return tf_text
print(compute_tf(lst1))


corpus=[]
corpus.append(lst)
corpus.append(lst1)
corpus.append(lst2)

print(corpus)

word=input("Введите слово ")

def compute_idf(word,corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

print(compute_idf(word,corpus))



def IDF(corpus):
N = len(corpus)
idflist = []
for doc in corpus:
	for i, val in doc.items():
		if val > 0:
			idflist[i] +=1
for i, val in idflist.items():			
	idflist[i] = math.log10(N / float(val))
return idflist





