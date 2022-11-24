from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

def match(word1, word2):
    '''Retorna la interseccion de los synsets entre cada par de palabras recibidas'''
    lemmatizer = WordNetLemmatizer()
    word1 = lemmatizer.lemmatize(word1)
    word2 = lemmatizer.lemmatize(word2)
    word1_synsets = wn.synsets(word1)
    word2_synsets = wn.synsets(word2)

    return list(set(word1_synsets) & set(word2_synsets))

print(match('ice', 'icing'))
print(match('involvement', 'interest'))
print(match('hot', 'spicy'))
print(match('duck', 'evade'))