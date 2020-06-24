from nltk.book import *
import matplotlib
import numpy
#imports sample texts
'''
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
'''

print(text1.concordance("monstrous"))#prints the contexts of the string

print(text1.similar("monstrous"))#prints words that appear in a simialr context

print(text2.common_contexts(["monstrous", "very"]))#prints common contexts between two words

print(text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"]))# creates a dispersion plot of the given words, needs matplotlib and numpy

print(len(text3))#gets length of text

print(sorted(set(text3))) #prints, in order, every unique token in set3

print((100 * text4.count('a') / len(text4)))    #gets percentage of the text is that token

fdist1 = FreqDist(text1)    #creates a frequency distribution

print(fdist1.most_common(50))   #prints 50 most common values

print(fdist1['whale'])  #frequency of whale

'''
Next, let's look at the long words of a text; perhaps these will be more characteristic and informative.
For this we adapt some notation from set theory. We would like to find the words from the vocabulary of the text that are more than 15 characters long.
Let's call this property P, so that P(w) is true if and only if w is more than 15 characters long.
Now we can express the words of interest using mathematical set notation as shown in (1a).
This means "the set of all w such that w is an element of V (the vocabulary) and w has property P".

(1)		
a.		{w | w ∈ V & P(w)}

b.		[w for w in V if p(w)]
'''

V = set(text1) #unqiue values in text1

long_words = [w for w in V if len(w) >15]   # lists of words if length of words is more than 15

print(long_words)

#getting long, frequent words


fdist5 = FreqDist(text5)    #frequency distrinution for chat corpora

long_common_words = sorted([w for w in set(text5) if len(w) > 7 and fdist[w] > 7])
# a list of tokens that are longer than 7 charcaters and occur more than 7 times in the text


#Bigrams
'''
A collocation is a sequence of words that occur together unusually often. Thus red wine is a collocation, whereas the wine is not.
A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, maroon wine sounds definitely odd.

To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as bigrams. This is easily accomplished with the function bigrams()
'''

print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))
#prints [('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]


'''
Here we see that the pair of words than-done is a bigram, and we write it in Python as ('than', 'done').
Now, collocations are essentially just frequent bigrams, except that we want to pay more attention to the cases that involve rare words.
In particular, we want to find bigrams that occur more often than we would expect based on the frequency of the individual words.
The  collocations() function does this for us. We will see how it works later.
'''


print(text4.collocations()) #prints common word pairs

'''
fdist = FreqDist(samples)	create a frequency distribution containing the given samples
fdist[sample] += 1	increment the count for this sample
fdist['monstrous']	count of the number of times a given sample occurred
fdist.freq('monstrous')	frequency of a given sample
fdist.N()	total number of samples
fdist.most_common(n)	the n most common samples and their frequencies
for sample in fdist:	iterate over the samples
fdist.max()	sample with the greatest count
fdist.tabulate()	tabulate the frequency distribution
fdist.plot()	graphical plot of the frequency distribution
fdist.plot(cumulative=True)	cumulative plot of the frequency distribution
fdist1 |= fdist2	update fdist1 with counts from fdist2
fdist1 < fdist2	test if samples in fdist1 occur less frequently than in fdist2
'''


#oepning other corpus

from nltk import gutenberg
print(gutenberg.fileids()) # prints file ids in the corpus from http://www.gutenberg.org/

# to examine data from the text, like above, open a text in the following way:
#emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))























