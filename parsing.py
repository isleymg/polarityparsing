import nltk
from nltk import Nonterminal, nonterminals, Production, CFG
import os
from nltk.parse import stanford
import itertools
from nltk.tree import *

execfile('C:\\Users\\Isley\\polarityparsing\\polarities.py')

# Test sentences
test = "Yesterday I met a girl that kept touching me on the arm without me wanting her to."
test1 = "She was lost and lonely despite being admired by most for her power."

# Stanford NLP Parser

os.environ['STANFORD_PARSER'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'

java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

parser = stanford.StanfordParser(model_path='C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars\\englishPCFG.ser.gz')
#sentences = parser.raw_parse_sents([test1, test2]) for parsing multiple sents

sentences = parser.raw_parse(test)

sentList = [list(i)[0] for i in sentences]

#sentList[0] is the tree object for the whole sentence
tree = sentList[0]
ptree = ParentedTree.convert(tree)

#len(sentList)      == 0
#len(sentList[0])   == 3
for i in range(len(sentList[0])):
    print(i, sentList[0][i])

from nltk import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
#wordnet_lemmatizer.lemmatize('creating','v')    # u'create'
#tokens = nltk.word_tokenize(test1)

#TODO:
#for each in sentList: treeparse(sentList)

'''
def treeparse(sentTree):
    for i in range(len(sentTree)):
    
        #if type(sentTree[i]) == nltk.tree.Tree:
            #return treeparse(phrase[0])
        if len(sentTree[i]) > 1:
            return treeparse(sentTree[i])
        else:
            lemPolarity = 0
            if len(sentTree[i])== 1 and type(sentTree[i][0]) == unicode:
            lem = wordnet_lemmatizer.lemmatize(sentTree[i][0])
            if lem in anewDict.keys():
                lemPolarity = anewDict[lem]
            #assign polarity
'''
def assignPolarity(ptree):
    '''Takes in a ParentedTree object that has no children and returns
    the polarity value of the lemmatized word token in it'''
    polarity = anewDict[wordnet_lemmatizer.lemmatize(ptree[0], ptree[0].label())]
    return polarity

def numOfSubtrees(ptree):
    '''Takes in a ParentedTree object and returns the number of subtrees it has'''
    return len(list(ptree.subtrees()))
        
#len(ptree) == 3
def parseSent(ptree):
    for i in range(len(ptree)):

        #Base case, if the subtree has no children
        subtree = ptree[i]
        if numOfSubtrees == 0:
            return assignPolarity(subtree)

        #Otherwise, if the subtree DOES have children
        elif numOfSubtrees == 1:
            return parseSent(subtree.subtrees())

        childList = []
        elif numOfSubtrees > 1:
            for childtree in subtree:
                childList.append(parseSent(childtree))

    return combinePolarity(childList)

def adjust(item1, item2):
    '''Makes an adjustment for modifiers in a sentence'''
    pass

def running average(item1, item2):
    average = it

def combinePolarity(childrenlist):
    #If the list has no modifiers in it, average together
                
            
        





        
##        #Case where subtree has no other siblings
##        if subtree.right_sibling() == None:
##            assignPolarity(subtree)
##
##            #Traverse upwards based on parent indexes?
##
##        #Case where subtree does have siblings
##        if subtree.right_sibling() != None: 
##            return parseSent(subtree)

##phraseSent
###no children
## base case: return polarity
##
### else has children --> last to first
##for each child:
##childlist append Parseesent(sehild)
##combine polarity function
##                        

'''
new list created for each subtree that has children (that don't have other children)
'''        
                        

    


treeSent = sentList[0]

#ptree.draw() will draw a diagram in a new window


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
