#!/usr/bin/env python

import string
import random

file = open('textfile', 'r')
text = file.read().upper()
file.close

file = open('1kMostCommonWords', 'r')
commons = set([file.read().upper()])
file.close

wordset = set([word.strip(string.punctuation) for word in text.split()])

wordset-commons

print(random.sample(wordset, 2))
