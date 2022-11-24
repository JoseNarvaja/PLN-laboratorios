from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def lesk_lemma(context_sentence, ambiguous_word, pos=None, synsets=None):

    lemmatizer = WordNetLemmatizer()

    context = set(context_sentence)

    if synsets is None:
        if pos:
            ambiguous_word = lemmatizer.lemmatize(ambiguous_word, pos)
        synsets = wordnet.synsets(ambiguous_word)

    if pos:
        ambiguous_word = lemmatizer.lemmatize(ambiguous_word, pos)
        synsets = [ss for ss in synsets if str(ss.pos()) == pos]

    if not synsets:
        return None

    _, sense = max(
        (len(context.intersection(ss.definition().split())), ss) for ss in synsets
    )

    return sense
