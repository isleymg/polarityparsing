'''
polarities.py
- Use NLTK Python SentimentAnalyzer as baseline for score comparisons
- Interface with both csv files of word sentiment scores -- valence mean
- scale from -1 to 1 for all three 
- Watson API for sentiment analysis (later)
'''
import csv
import os
os.chdir('C:\\Users\\Isley\\polarityparsing')


anewDict = {}
with open('anew.csv', 'rb') as anewFile:
	anewRaw = csv.reader(anewFile)
	for row in anewRaw:
		anewDict[row[0]] = row[1]


# print(anewDict.items())

warrinerDict = {}
with open('warriner.csv', 'rb') as warrinerFile:
	warrinerRaw = csv.reader(warrinerFile)
	for row in warrinerRaw:
		warrinerDict[row[0]] = row[1]


print('POLARITY CHARTS IMPORTED')
