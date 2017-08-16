'''
Use one of the predefined similarity measures to score the similarity 
of each of the following pairs of words. 
Rank the pairs in order of decreasing similarity.
 How close is your ranking to the order given here, 
 an order that was established experimentally by 
 (Miller & Charles, 1998): 
 car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, 
 asylum-madhouse, magician-wizard, midday-noon, furnace-stove, 
 food-fruit, bird-cock, bird-crane, tool-implement, brother-monk, 
 lad-brother, crane-implement, journey-car, monk-oracle, 
 cemetery-woodland, food-rooster, coast-hill, forest-graveyard, 
 shore-woodland, monk-slave, coast-forest, lad-wizard, 
 chord-smile, glass-magician, rooster-voyage, noon-string.
'''


import nltk
from nltk.corpus import wordnet as wn

if __name__ == '__main__':
	similarList = ["car-automobile","gem-jewel","journey-voyage","boy-lad","coast-shore","asylum-madhouse","magician-wizard","midday-noon","furnace-stove","food-fruit","bird-cock","bird-crane","tool-implement","brother-monk","lad-brother","crane-implement","journey-car","monk-oracle","cemetery-woodland","food-rooster","coast-hill","forest-graveyard","shore-woodland","monk-slave","coast-forest","lad-wizard","chord-smile","glass-magician","rooster-voyage","noon-string"]
	for n in similarList:
		n_1 = wn.synset(n.split('-')[0] + '.n.01')
		n_2 = wn.synset(n.split('-')[1] + '.n.01')
		print(n + ":")
		print((n_1).path_similarity(n_2))

