from nltk.corpus import stopwords
import StemVectorizer

spanish_stopwords = stopwords.words('spanish')
stem = StemVectorizer.StemVectorizer(min_df=1, stop_words=spanish_stopwords)
stem_analyze = stem.build_analyzer()

def mostrar(list):
    for tok in list:
        print(tok)

oracion = "John compro papas y zanahorias"
print(f"Oración 1: {oracion}")
Y = stem_analyze(oracion)
mostrar(Y)

oracion = "Los animales se juntaban en el parque"
print(f"\nOración 2: {oracion}")
Y = stem_analyze(oracion)
mostrar(Y)
