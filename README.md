# fictional-fiesta

at the moment, this codename generator will generate a random codename when given two files.
one file that has a bunch of text in it that you want to sample from (I am using Eisenhower’s military-industrial speech). the other file is a list of the 1000 most common works (not a requirement, but “a the” would make a pretty stupid code name).
the sample file is “foobar” and the common words is “1kMostCommonWords”
then this code will remove all the common words from the text, and spit out two random words from what’s left
which made me realize what I really want is an adjective and a noun. so I’m looking into part-of-speech classification, but that’s a bit much at the moment.

