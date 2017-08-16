'''
What is the branching factor of the noun hypernym hierarchy? 
I.e. for every noun synset that has hyponyms — 
or children in the hypernym hierarchy — 
how many do they have on average? 
You can get all noun synsets using wn.all_synsets('n').

hypernym
a word whose meaning includes a group of other words:
The first hypernyms for dog that come to mind would be animal or pet.
'''
'''
def group_branching_factor(group, relation) -> float:
	n_hyponyms = 0
	total_hyponyms = 0
	for n in wn.all_synsets(group):
		if len(noun.relation())> 0:
			total_hyponyms += 1
			n_hyponyms += len(noun.relation())
	return n_hyponyms/total_hyponyms

if __name__ == "__main__":
	print(group_branching_factor('n', hyponyms))
'''

import nltk
from nltk.corpus import wordnet as wn

if __name__ == "__main__":
	n_hyponyms = 0
	total_hyponyms = 0
	for n in wn.all_synsets('n'):
		if len(n.hyponyms())> 0:
			total_hyponyms += 1
			n_hyponyms += len(n.hyponyms())
	print(n_hyponyms/total_hyponyms)




# i COULD do a one-line with 2 listcomps, but that just feels WAY too inefficient
#print sum([ slen(noun.hyponyms()) for 
    
    
    # Answer
    # In the current copy of WordNet:
    # nouns with hyponyms: 16693
    # total hyponyms: 75850 
    # branching factor: 4.54382076319