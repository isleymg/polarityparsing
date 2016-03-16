import nltk
import os
from nltk.parse import stanford
from nltk.corpus import wordnet
from nltk.tree import *

# execfile('C:\\Users\\Isley\\polarityparsing\\polarities.py')
anewDict = {'lost': -0.646, 'lonely': -0.7075, 'admired': 0.685, 'power': 0.385, 'not': -0.5}
print(anewDict)

# Test sentences
test0 = "Yesterday I met a girl that kept touching me on the arm without me wanting her to."
test = "She was lost and lonely despite being admired by most for her power."
test1 = "She was not admired."
# Stanford NLP Parsers
os.environ['STANFORD_PARSER'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'
java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

parser = stanford.StanfordParser(model_path='C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars\\englishPCFG.ser.gz')
#sentences = parser.raw_parse_sents([test1, test2]) for parsing multiple sents

sentences = parser.raw_parse(test1)
sentList = [list(i)[0] for i in sentences]

#sentList[0] is the tree object for the whole sentence
tree = sentList[0]
print(tree)
ptreeTEST = ParentedTree.convert(tree)


for i in range(len(sentList[0])):
    print(i, sentList[0][i])

from nltk import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#wordnet_lemmatizer.lemmatize('creating','v')    # u'create'
#tokens = nltk.word_tokenize(test1)

def get_wordnet_pos(treebank_tag):
    if treebank_tag[0] == 'J':
        return wordnet.ADJ
    elif treebank_tag[0] == 'V':
        return wordnet.VERB
    elif treebank_tag[0] == 'N':
        return wordnet.NOUN
    elif treebank_tag == 'R':
        return wordnet.ADV
    else:
        return ''

def assignPolarity(ptree):
    '''Takes in a ParentedTree object that has no children and returns
    the polarity value of the lemmatized word token in it'''
    try:
        polarity = anewDict[wordnet_lemmatizer.lemmatize(ptree[0], get_wordnet_pos(ptree.label()))]
    except KeyError:
        try:
            polarity = anewDict[ptree[0]]
        except KeyError:
            polarity = 0
            print('Not found: ' + ptree[0])
            
    return polarity

def numOfSubtrees(tree):
    '''Takes in a ParentedTree object and returns the number of subtrees it has'''
    result = len(list(tree.subtrees()))
    return result
        
childList = []

subList = []

def parseOne(subtree):
    #third loop for lengths that are counted the same
    if len(list(subtree.subtrees())) > 1:
        word = subtree[0][0]
        label = subtree[0].label()
        subList.append((subtree[0][0], subtree[0].label(), assignPolarity(subtree[0])))
    else:
        subList.append((subtree[0], subtree.label(), assignPolarity(subtree)))
    return subList

def parse(subtree):
    # second loop for each subtree within main subtree
    if subtree.__len__() == 1:
        parseOne(subtree)
    else:
        for i in range((subtree.__len__())-1,0,-1):
            if subtree[i].__len__()==1:
                parseOne(subtree[i])
                
            else:
                parse(subtree[i])
                
    
def parseSent(ptree):
    #first loop for each subtree under main sentence
    for i in range((ptree.__len__())-1,0,-1):
        subtree = ptree[i]
        parse(subtree)
        
        # IF hasModifiers, use adjust function
        # ELSE use listAverage
        
    return combinePolarity(childList)


def adjust(item1, item2):
    '''Makes an adjustment for modifiers in a sentence'''
    pass

def listAverage(itemList):
    num = 0
    for word in itemList:
        num += word[2]
    return ( num/ float(len(itemList)))

def runningAverage(itemList, item2):
    return ((listAverage(itemList) + item2[2])/(len(itemList)+1))

modifiersList = ["without", "despite"]

def hasModifiers(list1):       
    for element in list1:
        if element in modifiersList:
            return True
    return False

def combinePolarity(childList):
    #If the list has no modifiers in it, average together
    if not hasModifiers(childList):
        return listAverage(childList)
    else:
        return runningAverage(childList)


'''
new list created for each subtree that has children (that don't have other children)
''' 

'''
TESTING TO SEE WHICH TOKENS ARE IN LEMLIST
for each in lemlist:
	if each in anewDict.keys():
		print(anewDict[each], each)

#Results from anewDict	
('-0.545', 'lost')
('-0.7075', 'lonely')
('0.685', 'admired')
('0.385', 'power')


TODO LATER
# SentiWordNet
from nltk.corpus import sentiwordnet as swn
##print(list(swn.senti_synsets('slow')))
happy = list(swn.senti_synsets('happy', 'a'))
##print(happy)
'''

if __name__ == "__main__":
    parseSent(ptreeTEST)
    print("---end---")
