
# -*- coding: utf-8 -*-
import pymorphy2
import nltk
import copy
import collections
import math
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
        for synset in wikiwordnet.get_synsets(i):
            print(synset)
            for word in synset.get_words():
                print(word.lemma())
                yield word.lemma()
##############
def pars_tag(token):
    p = morph.parse(token)
    for itag in p:
        yield (itag.tag.cyr_repr, itag.score)

1
def find_t(tokens, tags, exept):
    for token in tokens:
        token_tag = sorted(list(set(pars_tag(token))), key=lambda i: i[1])
        #token_tag = [t[0] for t in _token_tag]
        tokset = set()
        if tags == ['ГЛ'] and exept == {1} and (token == '-' or token == '–'):
            tokset.add('есть')
        for i in token_tag:
            if set(tags) <= set(i[0].split(',')) and  not set(exept).issubset(set(i[0].split(','))):
                tokset.add((token, i[1]))
        if tokset != set():
            yield sorted(list(tokset), key=lambda i: i[1])
1



def fpredication(invar_list):#[['Солнце светило ярко', ' мальчик пошёл быстрее'], ['Солнце светило ярко _ мальчик пошёл быстрее']]
    for invariant in invar_list:
        pred_list=[]
        for part in invariant:
            tokens = nltk.word_tokenize(part)
            sush = list(find_t(tokens, {'СУЩ', 'им'},{'аббр'}))
            sush += list(find_t(tokens,{'МС', 'им'}, {1}))
            sush += list(find_t(tokens,{'ИНФ'}, {1}))
            gl = find_t(tokens, ['ГЛ'], {1})
            obj = list(find_t(tokens, {'СУЩ'}, {1}))
            obj += list(find_t(tokens,{'МС'}, {1}))
            obj += list(find_t(tokens,{'МС'}, {1}))
            pred_list.append((sush, list(gl), obj))
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
        self.tokens_sentences_list=[]
        for string in self.str_sentences_list:
            string = string.replace(',', '')
            self.tokens_sentences_list.append(nltk.word_tokenize(string))

        for str_sentence in self.str_sentences_list:
            cls_sentence = _sentence(str_sentence)
            self.cls_sentences_list.append(cls_sentence)


class _sentence():
    def __init__(self, str):
        self.invariant_tree = (self.rekurs([str]))
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n', (self.rekurs([str])))
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
        print('in', list)
        for i in list:
            if type(i) is str:
                if self.zpt(i):
                    if self.spp(i):
                        list.remove(i)
                        self.splitcomplex(list, i)
                    elif self.ssp(i):
                        list.remove(i)
                        self.splitcomplex(list, i)
                        self.homosplit(list, i)
                    else:
                        list.remove(i)
                        self.splitcomplex(list, i)
                        self.homosplit(list, i)
            else:
                print('in2', list)
                self.rekurs(i)
        return list



    def splitcomplex(self, list, i):
        index = i.find(',')
        l1 = i[index+1:]
        l2 = i[:index]
        list.append(l2)
        list.append([l1])



    def homosplit(self, list, i):#dobavit simvol_
        i1 = i[0:i.find(',')]
        i2 = i[i.find(',')+1:]
        i3 = i1+'_'+i2
        new = i3#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111111111
        list.append ([new])

#условия

    def ssp(self, i):
        token = nltk.word_tokenize(i)
        if token[token.index(',')+1] in ssps_set:
            return True
        else:
            return False

    def spp(self, i):
        token = nltk.word_tokenize(i)
        index1 = 0
        if len(token)-token.index(',')>6:
            r = 6
        else:
            r = len(token)-token.index(',')

        for i in range(r):
            index1+=1
            soius = token[token.index(',')+1:token.index(',')+index1+1]
            s = ' '.join(soius)
            if s in spps_set:
                return True

        else:
            return False

    def zpt(self, i):
        if ',' in i:
            return True
        else:
            return False
#синтез инварианта по дереву
    def sintes(self, list):
        if check(list):
            for i in range(len(list)):
                list.pop(0)
            return []
        try:
            if list[1] == []:
                list.pop(1)
            out = self.sintes(list[1])
            if out == []:
                if check(list):
                    for i in range(len(list)):
                        list.pop(0)
                    return []
            else:
                if not out[0].startswith(list[0]):
                    out.insert(0, list[0])
            return out
        except IndexError:
            out = [list.pop(0)]
            return out
    


#функция для вывода данных
def out_print(t):
    t.str_sentences_list
    for i in t.cls_sentences_list:
        print('=======================================================================================\nsentence = ', t.str_sentences_list[t.cls_sentences_list.index(i)], '\ntree=',i.invariant_tree_copy)
        for n in i.invariant_list:
            print('part=', n, '\n')
    print('\n'*5)
    for i in t.cls_sentences_list:
        print(i.semantic)
        print('=======================================================================================\n\nпредложение = ', t.str_sentences_list[t.cls_sentences_list.index(i)],'\nвсе возможные варианты синтаксического разбора:', i.invariant_list)
        for n in i.semantic:
            print('============================================================','\nвариант синтаксического разбора', i.invariant_list[i.semantic.index(n)])
            for sempart in n:
                print('\nsemantic part:', i.invariant_list[i.semantic.index(n)][n.index(sempart)], '\nsubject-', sempart[0], '\npredicat-', sempart[1], '\nobject', sempart[2])



spps_set = {'поскольку', 'в связи с тем что', 'как только', 'покамест', 'несмотря на то что', 'когда', 'для того чтобы', 'затем что', 'пока', 'покуда не', 'прежде нежели', 'хоть бы', 'дабы', 'даром что', 'только', 'а то', 'оттого что', 'когда б', 'пускай бы', 'лишь только', 'словно', 'нежели', 'в то время как', 'покамест не', 'пока не', 'хотя', 'по мере того как', 'будто', 'пускай', 'только что', 'коль скоро', 'коли', 'с тех пор как', 'покуда', 'чем', 'ввиду того что', 'правда', 'точно', 'так как', 'хотя бы', 'хоть', 'кабы', 'так что', 'а не то', 'лишь бы', 'только бы', 'едва', 'благодаря тому что', 'как будто', 'невзирая на то что', 'затем чтобы', 'если', 'чуть', 'что', 'когда бы', 'лишь', 'как будто бы', 'если б', 'прежде чем', 'чтоб', 'ибо', 'как', 'добро бы', 'чуть лишь', 'в силу того что', 'если бы', 'пусть', 'подобно тому как', 'между тем как', 'потому что', 'после того как', 'раз', 'чуть только', 'будто бы', 'до того как', 'ли', 'едва только', 'с тем чтобы', 'чтобы', 'тогда как', 'вследствие того что'}
ssps_set = {'и', 'да', 'тоже', 'также', 'а', 'но', 'зато', 'зато', 'или', 'либо'}

text_test1 = "Поздней осенью выпадает первый снег. Он изменяет всё вокруг. Пушистые снежинки осторожно касаются земли, и она одевается в белую шубку. Загораются и блестят разноцветные искорки инея. Вода темнеет среди прибрежных зарослей. Как прекрасна берёзовая роща! Веточки покрыты хлопьями, но от любого прикосновения снежинки осыпаются. В ельнике снег так засыпал деревья, что ты их не узнаешь. Ёлочка становится похожей на причудливую снежную бабу. Всюду виднеются следы лесных зверей. В зимние дни дома не сидится. Дети и взрослые выходят на прогулку. Каждый хочет почувствовать свежесть первого морозца, сыграть в снежки. «Здравствуй, зима!» — радостно говорят люди"
tosamoe = _text(text_test1)


print('\n\n to chto nado', tosamoe.tokens_sentences_list)

tokenlist = []
filtered_words = [word for word in word_list if word not in ['и', "но"]]
for l in filtered_words:
    for t in l:
        tokenlist.append(t)

def compute_tf(lst):
    tf_text=collections.Counter(lst)
    for i in tf_text:
        tf_text[i]=tf_text[i]/float(len(lst))
    return tf_text
print(compute_tf(tokenlist))

print('idf')
def compute_idf(word,corpus):
    return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))
for i in tokenlist:
    print(i, compute_idf(i, tosamoe.tokens_sentences_list))

tfdf_dict=compute_tf(tokenlist)
for i in tfdf_dict:
    tfdf_dict[i]= tfdf_dict[i]*compute_idf(i, tosamoe.tokens_sentences_list)
print(tfdf_dict)