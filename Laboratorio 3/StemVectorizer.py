from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer

class StemVectorizer(CountVectorizer):

    def build_analyzer(self):
        analyzer = super(StemVectorizer, self).build_analyzer()
        spanish_stemmer = SnowballStemmer('spanish')
        return lambda doc: (spanish_stemmer.stem(w) for w in analyzer(doc))
