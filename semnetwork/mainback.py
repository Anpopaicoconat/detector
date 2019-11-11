
# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import copy
from wiki_ru_wordnet import WikiWordnet
wikiwordnet = WikiWordnet()
morph = pymorphy2.MorphAnalyzer()
################
def synonymscheck (inlist, keylist):
    corrans = 0 #Correct Answers (Верные соответствия)
    for i in inlist:
        synsets = wikiwordnet.get_synsets(i)
        for n in wikiwordnet.get_synsets(keylist[inlist.index(i)]):
            if n in synsets:
                corrans +=1
                print(corrans,'/3')
            else:
                pass
###############
def getlemma (inlist):
    corrans = 0 #Correct Answers (Верные соответствия)
    for i in inlist:
        synsets = wikiwordnet.get_synsets(i)
        #print(synsets)
        for synset in wikiwordnet.get_synsets(i):
            print(synset)
            for word in synset.get_words():
                print(word.lemma())
                yield word.lemma()
##############
def pars_tag(token):
    p = morph.parse(token)
    for itag in p:
        yield itag.tag.cyr_repr


def find_t(tokens, tags):#не возвращать одни и те же
    for token in tokens:
        token_tag = set(pars_tag(token))
        for i in token_tag:
            if set(tags) <= set(i.split(',')):
                yield token
1



def fpredication(invar_list):
    for invariant in invar_list:
        pred_list=[]
        for part in invariant:
            tokens = nltk.word_tokenize(part)
            sush = list(find_t(tokens, {'СУЩ', 'им'}))
            #sush2 = list(find_t(tokens,{'М'}))
            #print('sush1, sush2', sush1, sush2)
            gl = find_t(tokens, ['ГЛ'])
            pred_list.append((sush, list(gl)))
        yield pred_list
####################################

def check(list):
    if len(list) == 2:
        if (type(list[0]) is str) and (list[1] == []):
            return True
        else:
            return False
    else:
        return False

class _text():
    def __init__(self, text):
        self.str_sentences_list = text.split('.')#список предложений в строковом типе
        self.cls_sentences_list = []#список объектов класса _sentence
        for str_sentence in self.str_sentences_list:
            cls_sentence = _sentence(str_sentence)
            self.cls_sentences_list.append(cls_sentence)


class _sentence():
    def __init__(self, str):
        self.invariant_tree = (self.rekurs([str]))
        self.invariant_tree_copy = copy.deepcopy(self.invariant_tree)
        self.invariant_list = []
        while self.invariant_tree != []:
            invariant = self.sintes(self.invariant_tree)
            if invariant != []:
                self.invariant_list.append(invariant)
                #print('\n invariant', invariant, '\n')
        self.semantic = list(fpredication(self.invariant_list))
#        self.semanticex = 1#semanticex(self.semantic)
#    def semanticex(self, semantic):
#        for sentpart in semantic:
#            for varpart in sentpart:
#                for word in varpart:
#                    print(word)




    def rekurs(self, list):
        #list = copy.deepcopy(list)
        for i in list:
            if type(i) is str:
                if self.spp(i):
                    list.remove(i)
                    self.splitcomplex(list, i)
                elif self.uslovie(i):
                    list.remove(i)
                    self.splitcomplex(list, i)
                    self.homosplit(list, i)
            else:
                self.rekurs(i)
        return list



    def splitcomplex(self, list, i):
        index = i.find(',')
        l1 = i[index+1:]
        l2 = i[:index]
        list.append(l2)
        list.append([l1])



    def homosplit(self, list, i):#dobavit simvol_
        new = i.replace(',', " _")
        list.append ([new])

#условия

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

    def souzposle(self, i):
        token = nltk.word_tokenize(i)
        tokenposle = token[token.index(',')+1]
        tokenposle = []
        p = morph.parse(token)
        for itag in p:
            tokenposle.append (itag.tag.cyr_repr)
        for i in tokenposle:
            if 'СОЮЗ' in i:
                return True
#синтез инварианта по дереву
    def sintes(self, list):
        #print('list=', list)
        if check(list):
            for i in range(len(list)):
                #print('pop')
                list.pop(0)
            return []
        try:
        
            if list[1] == []:
                list.pop(1)
            out = self.sintes(list[1])
            if out == []:
                if check(list):
                    for i in range(len(list)):
                        #print('pop')
                        list.pop(0)
                    return []
                #print('аут когда предыдущий пустой')
            else:
                if not out[0].startswith(list[0]):#что бы не вносились повторяющиеся части
                    out.insert(0, list[0])
                #print('out когда предыдуший не пустой')
            return out
        except IndexError:
            #print('out единственная строка', [list[0]])
            out = [list.pop(0)]
        
            return out
    


#функция для вывода данных
def out_print(t):
    t.str_sentences_list
    #print(t.cls_sentences_list[0].invariant_tree_copy, '\n\n')
    #print('invarlist', t.cls_sentences_list[0].invariant_list)
    for i in t.cls_sentences_list:
        for n in i.invariant_list:
            print('part=', n, '\n')
    for i in t.cls_sentences_list:
        print('semantic-', i.semantic)
    #print('semantic=', t.cls_sentences_list[0].semantic)
def out_print(t):
    t.str_sentences_list
    for i in t.cls_sentences_list:
        print('=======================================================================================\nsentence = ', t.str_sentences_list[t.cls_sentences_list.index(i)], '\ntree=',i.invariant_tree_copy)
        for n in i.invariant_list:
            print('part=', n, '\n')
    for i in t.cls_sentences_list:
        print('=======================================================================================\n\nsentence = ', t.str_sentences_list[t.cls_sentences_list.index(i)])
        for n in i.semantic:
            print('============================================================')
            for sempart in n:
                print('semantic part:', 'subject-', sempart[0], 'predicat-', sempart[1], 'object', sempart[2])
   


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

spps_list = ['таккак', 'потомучто', 'поскольку', 'оттогочто', 'ввидутогочто', 'благодарятомучто', 'вследствиетогочто', 'всвязистемчто', 'всилутогочто', 'ибо', 'затемчто', 'такчто', 'ато', 'ането', 'чтобы', 'чтоб', 'длятогочтобы', 'стемчтобы', 'затемчтобы', 'дабы', 'если', 'еслибы', 'еслиб', 'раз', 'ли', 'кольскоро', 'ежели(бы', 'б)', 'коли', 'кабы', 'когдабы', 'когдаб', 'хотя', 'хоть;даромчто;толькобы', 'лишьбы;несмотрянаточто', 'невзираянаточто;хотябы', 'хотьбы', 'пусть', 'пускай;втовремякак', 'междутемкак', 'тогдакак;добробы', 'пускайбы;только', 'правда', 'едва', 'едватолько', 'кактолько', 'как', 'когда', 'лишь', 'лишьтолько', 'померетогокак', 'послетогокак', 'стехпоркак', 'пока', 'покане', 'покамест', 'покаместне', 'покуда', 'покудане', 'прежденежели', 'преждечем', 'только', 'толькочто', 'чутьлишь', 'чуть', 'чутьтолько', 'дотогокак', 'втовремякак', 'как', 'что', 'будто', 'будтобы', 'какбудто', 'какбудтобы', 'словно(как)', 'подобнотомукак', 'точно', 'ровно(как)', 'чем', 'нежели', 'что', 'чтобы', 'будтобы', 'как']
spps_list=['ибо', 'чтобы', 'чтоб', 'дабы', 'если', 'раз', 'ли', 'ежели', ' коли', 'кабы', ' хотя', \
    'хоть', 'пусть', 'пускай', 'как', 'покуда', 'чуть', 'что', 'чем', 'поскольку'] #требуется дороботка



text_test1 = 'первое, что второе, третье, четвертое, что пятое, шестое'

#text_test1 = 'Мальчик купил мороженое. Мороженое было вкусным. Солнце светило ярко, мальчик пошёл быстрее. Мальчик заплакал, поскольку мороженое расстаяло'#подлежащее не всегда стоит в именительном падеже!!!
#text_test1 = 'Барболин сказал солдату, сидевшему на сиденье машины, открыл дверь'

t = _text(text_test1)

out_print(t)
