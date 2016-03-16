# polarityparsing

# Current Implementation: 
This project is a tool that takes sentences as input and parses them using the Stanford Parser, assigns polarities to lemmatized tokens from bottom up approach. Takes account of modifiers and adjustments for how to deal with modifiers. 

Taken from the Stanford Natural Language Processing Group:
The [Stanford Parser] implements a factored product model, with separate PCFG phrase structure and lexical dependency experts, whose preferences are combined by efficient exact inference, using an A* algorithm. Or the software can be used simply as an accurate unlexicalized stochastic context-free grammar parser. Either of these yields a good performance statistical parsing system. A GUI is provided for viewing the phrase structure tree output of the parser.

More about the http://nlp.stanford.edu/software/lex-parser.shtml

# Run Requirements:
In order to run this project, you will need to download the Stanford Parser, which is written in Java, and save it to your local directory. Then, change the directory locations under "# Stanford NLP Parsers Location" to the directory in which your Standford Parser files are saved. Learn how to download here: http://stackoverflow.com/questions/13883277/stanford-parser-and-nltk

# Future Updates:
In the future we will work on different types of adjustements for modifier words, such as multiplying by a coefficient. We may also implement a length penalty that will take into consideration how many total words make up a sentence that contains a modifier. 
