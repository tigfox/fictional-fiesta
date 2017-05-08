#!/usr/bin/env python

import random
import nltk

file = open('textfile', 'r')
text = file.read()
file.close

sentences = nltk.sent_tokenize(text)
nouns = []
adjectives = []

for sentence in sentences:
    for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN' or pos == 'NNS'):
            nouns.append(word)
        if (pos == 'JJ'):
            adjectives.append(word)

nounset = set(nouns)
adjset = set(adjectives)

print("%s %s" % (str(random.sample(adjset, 1)[0]).upper(), str(random.sample(nounset, 1)[0]).upper()))

