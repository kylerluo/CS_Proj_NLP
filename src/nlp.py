sentence = 'The quick brown fox jumped over the lazy dog and the quick cat'
print("")
print("The sentence:")
print(sentence)
print("")
words = sentence.split(' ')
print("")
print('Tokenization example:')
print("")
print(words)
print("")
bigrams = [b for b in zip(words[:-1], words[1:])]
print("")
print('Text represenation bigram example:')
print("")
print(bigrams)
print("")
from collections import defaultdict
cfd = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(len(words) - 2):  # loop to the next-to-last word
    cfd[words[i].lower()][words[i+1].lower()] += 1

print("")
print('Conditional Frequency Distributions example')
print("")
print({k: dict(v) for k, v in dict(cfd).items()})
print("")
print("The most likely word after the is :", max(cfd['the']))
print("")

import nltk
grammar = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom
  Nom -> Adj Nom | N
  VP -> V NP | V S | V PP 
  PP -> P NP | P PP
  Det -> 'the'| 'The'
  N -> 'fox' | 'dog' | 'cat' 
  Adj  -> 'quick' | 'lazy' | 'brown'
  V ->  'jumped'|
  P -> 'over'
  """)
print("")
print('A part of speech tagging tree example')
print("Parsing the sentence: \"The quick brown fox jumped over the lazy dog\" with the context free grammar : ")
print(grammar)
print("")

rd_parser = nltk.RecursiveDescentParser(grammar)
print("The parsed syntax trees: \n")
for tree in rd_parser.parse('The quick brown fox jumped over the lazy dog'.split()):
    tree.pretty_print()