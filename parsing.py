import nltk
from nltk import Nonterminal, nonterminals, Production, CFG
import os
from nltk.parse import stanford
import itertools
from nltk.tree import *

execfile('C:\\Users\\Isley\\Anaconda\\NLTKexploration\\polarities.py')

# Test sentences
test1 = "Yesterday I met a girl that kept touching me on the arm without me wanting her to."
test2 = "She got a little too close for comfort."

# Stanford NLP Parser

os.environ['STANFORD_PARSER'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'
os.environ['STANFORD_MODELS'] = 'C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars'

java_path = "C:\\Program Files\\Java\\jdk1.8.0_60\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path

parser = stanford.StanfordParser(model_path='C:\\Users\\Isley\\Anaconda\\Lib\\site-packages\\nltk\\parse\\jars\\englishPCFG.ser.gz')
#sentences = parser.raw_parse_sents([test1, test2])

sentences = parser.raw_parse(test1)
print sentences

sentList = [list(i)[0] for i in sentences]

#sentList[0] is the tree object for the whole sentence
tree = sentList[0]
ptree = ParentedTree.convert(tree)

from nltk import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

#for each in sentList: treeparse(sentList)

'''
def treeparse(sentTree):
    for i in range(len(sentTree)):
        if type(sentTree[i]) == nltk.tree.Tree:
            treeparse(phrase[0])
        else:
            lemPolarity = 0
            type(sentTree[i]) == unicode:
            lem = wordnet_lemmatizer.lemmatize(phrase[0])
            if lem in anewDict.keys():
                lemPolarity = anewDict[lem]
            #assign polarity
        

'''

treeSent = sentList[0]

# GUI
for line in sentences:
    for sentence in line:
        print(sentence)
        sentence.draw()


    

# SentiWordNet
from nltk.corpus import sentiwordnet as swn
##print(list(swn.senti_synsets('slow')))
happy = list(swn.senti_synsets('happy', 'a'))
##print(happy)

