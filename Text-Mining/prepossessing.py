#import all necessary libraries
#from nltk.stem import PorterStemmer
#from nltk.tokenize import SpaceTokenizer

from nltk.corpus import stopwords
from functools import partial

from nltk import word_tokenize
from nltk.stem import SnowballStemmer


import unicodedata
#from gensim import corpora
#from gensim.models import TfidfModel
import re

texts = ['HOLA! esto es una test!!!',
         'café, chocolate, té ...',
         'Todo es divereciones.']


 
# initialize the instances for various NLP tools
# tokenizer = SpaceTokenizer()
# stemmer = PorterStemmer()


#tokenizer = word_tokenize()
stemmer = SnowballStemmer('spanish')
stopwords = set(stopwords.words('spanish'))

 
# steps
pipeline = [lambda word: unicodedata.normalize('NFKD', unicode(word, "utf-8")).encode('ASCII', 'ignore'),
            lambda word: re.sub('[^\w\s]', '', word),
            # lambda word: re.sub('[\d]', '', word),
            lambda word: word.lower(),
            lambda word: ' '.join(filter(lambda word: not (word in stopwords), tokenizer.tokenize(word))),
            # lambda word: ' '.join(map(lambda t: stemmer.stem(t), word_tokenize(word)))
           ]
 
# pipeline step-by-step
def preprocess_text(text, pipeline):
    if len(pipeline)==0:
        return text
    else:
        return preprocess_text(pipeline[0](text), pipeline[1:])
 
# preprocessing
preprocessed_texts = map(partial(preprocess_text, pipeline=pipeline), texts)

print(texts)
print(preprocessed_texts)
