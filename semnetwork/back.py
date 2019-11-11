
# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import string
morph = pymorphy2.MorphAnalyzer()

class _text():
    def __init__(self, text):
        self.str_sentences_list = text.split('.')#список предложений в строковом типе
        self.cls_sentences_list = []#список объектов класса _sentence
        for str_sentence in self.str_sentences_list:
            print('str_sentence=', str_sentence)
            cls_sentence = _sentence(str_sentence)
            self.cls_sentences_list.append(cls_sentence)


class _sentence():
    def __init__(self, str):
        print('инициация _sentence для str=', str,'\n\n')
        self.invariant = (self.rekurs([str]))

    def rekurs(self, list):
        print('rekurs для list=', list, '\n')
        count = 0
        while count < len(list):
            i = list[count]
            print("итерируемый объект=", i)
            if type(i) is str:
                if self.spp(i):
                    list.remove(i)
                    self.splitcomplex(list, i)
                elif self.uslovie(i):
                    list.remove(i)
                    self.splitcomplex(list, i)
                    self.homosplit(list, i)
                print('\n\nbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb\n\n')
                count+=1
            else:
                self.rekurs(i)
                print('\n\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n')
                count+=1



    def splitcomplex(self, list, i):
        index = i.find(',')
        l1 = i[index+1:]
        l2 = i[:index]
        list.append(l2)
        list.append([l1])



    def homosplit(self, list, i):
        i.replace(',', "_")
        list.append ([i])



    def spp(self, i):
        if ',' in i:
            token = nltk.word_tokenize(i)
            if token[token.index(',')+1] in spps_list:
                return True
            else:
                return False

    def uslovie(self,i):
        if ',' in i:
            return True
        else:
            return False

    def zpt(self,i):
        if ',' in i:
            return True
        else:
            return False

    def souzposle(self,i):
        token = nltk.word_tokenize(i)
        tokenposle = token[token.index(',')+1]
        tokenposle = []
        p = morph.parse(token)
        for itag in p:
            tokenposle.append (itag.tag.cyr_repr)
        for i in tokenposle:
            if 'СОЮЗ' in i:
                return True


spps_list = ['так как', ' потому что', ' поскольку', ' оттого что', ' ввиду того что', ' благодаря тому что',\
   ' вследствие того что', ' в связи с тем что', ' в силу того что', ' ибо', ' затем что', ' так что', ' а то',\
  ' а не то', ' чтобы', ' чтоб', ' для того чтобы', ' с тем чтобы', ' затем чтобы', ' дабы', ' если', ' если бы',\
 ' если б', ' раз', ' ли', ' коль скоро', ' ежели (бы', ' б)', ' коли', ' кабы', ' когда бы', ' когда б', ' хотя',\
' хоть; даром что; только бы', ' лишь бы; несмотря на то что', ' невзирая на то что; хотя бы', ' хоть бы', ' пусть',\
' пускай; в то время как', ' между тем как', ' тогда как; добро бы', ' пускай бы; только', ' правда', ' едва',\
' едва только', ' как только', ' как', ' когда', ' лишь', ' лишь только', ' по мере того как', ' после того как',\
' с тех пор как', ' пока', ' пока не', ' покамест', ' покамест не', ' покуда', ' покуда не', ' прежде нежели',\
' прежде чем', ' только', ' только что', ' чуть лишь', ' чуть', ' чуть только', ' до того как', ' в то время как',\
' как', ' что', ' будто', ' будто бы', ' как будто', ' как будто бы', ' словно (как)', ' подобно тому как', ' точно',\
' ровно (как)', ' чем', ' нежели', ' что', ' чтобы', ' будто бы', ' как']



text_test1 = 'первое, что второе, третье.'



_text(text_test1)
print('finish')
########
def check(list):
    if len(list) < 2:
        print('len(list) < 2 False')
        return False
    print('check list', list)
    for i in list:
        print('i=', i)
        if not(type(i) is str or i == []):
            print('not(type(i) is str or i == []) False', 'type str', type(i), '[]', i == [], type(i) is str or i == [])
            return False
    if type(list[0]) is str and list[1]==[]:
        print('True')
        return True


spps_list=['ибо', 'чтобы', 'чтоб', 'дабы', 'если', 'раз', 'ли', 'ежели', ' коли', 'кабы', ' хотя', \
    'хоть', 'пусть', 'пускай', 'как', 'покуда', 'чуть', 'что', 'чем', 'поскольку'] #требуется дороботка
spps_list_og = ['так как', ' потому что', ' поскольку', ' оттого что', ' ввиду того что', ' благодаря тому что',\
' вследствие того что', ' в связи с тем что', ' в силу того что', ' ибо', ' затем что', ' так что', ' а то',\
' а не то', ' чтобы', ' чтоб', ' для того чтобы', ' с тем чтобы', ' затем чтобы', ' дабы', ' если', ' если бы',\
' если б', ' раз', ' ли', ' коль скоро', ' ежели (бы', ' б)', ' коли', ' кабы', ' когда бы', ' когда б', ' хотя',\
' хоть; даром что; только бы', ' лишь бы; несмотря на то что', ' невзирая на то что; хотя бы', ' хоть бы', ' пусть',\
' пускай; в то время как', ' между тем как', ' тогда как; добро бы', ' пускай бы; только', ' правда', ' едва',\
' едва только', ' как только', ' как', ' когда', ' лишь', ' лишь только', ' по мере того как', ' после того как',\
' с тех пор как', ' пока', ' пока не', ' покамест', ' покамест не', ' покуда', ' покуда не', ' прежде нежели',\
' прежде чем', ' только', ' только что', ' чуть лишь', ' чуть', ' чуть только', ' до того как', ' в то время как',\
' как', ' что', ' будто', ' будто бы', ' как будто', ' как будто бы', ' словно (как)', ' подобно тому как', ' точно',\
' ровно (как)', ' чем', ' нежели', ' что', ' чтобы', ' будто бы', ' как']
