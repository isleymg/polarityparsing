import nltk
import os
from nltk.parse import stanford
from nltk.corpus import wordnet
from nltk.tree import *

# execfile('C:\\Users\\Isley\\polarityparsing\\polarities.py')
anewDict = {'lost': -0.646, 'lonely': -0.7075, 'admired': 0.685, 'power': 0.385}
print(anewDict)

# Test sentences
test0 = "Yesterday I met a girl that kept touching me on the arm without me wanting her to."
test = "She was lost and lonely despite being admired by most for her power."
test1 = "She was lost but not lonely."
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

def parse(subtree):
    
    if numOfSubtrees(subtree) == 1:
        childList.append((subtree[0], subtree.label(), assignPolarity(subtree)))
        print(childList)
        return childList

    #if numOfSubtrees(subtree) == 1:
        #return parse(subtree.subtrees())

    if numOfSubtrees(subtree) > 1:
        for childtree in subtree:
            parse(childtree)

def parseSent(ptree):
    """ childList is a list of tuples with values:
    'word', 'POS tag', and 'polarity' """
    print('childlist')
    print(childList)
    for i in range(len(ptree)):
        subtree = ptree[i]
        parse(subtree)
        
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

def hasModifiers(childList):        ## TAG for modifier? list of tuples
    for element in childList:
        if element in modifiersList:
            return True
    return False

def combinePolarity(childList):
    #If the list has no modifiers in it, average together
    if not hasModifiers(childList):
        return listAverage(childList)
    else:
        return runningAverage(childList)


        
##        #Case where subtree has no other siblings
##        if subtree.right_sibling() == None:
##            assignPolarity(subtree)
##
##            #Traverse upwards based on parent indexes?
##
##        #Case where subtree does have siblings
##        if subtree.right_sibling() != None: 
##            return parseSent(subtree)

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
