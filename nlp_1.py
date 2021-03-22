from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather"

blob = TextBlob(text)

# print(blob)

# print(blob.sentences)

# print(blob.words)

# Part of Speech Tagging
# print(blob.tags)

# print(blob.noun_phrases)

# Sentiment Analysis
# print(blob.sentiment)

# print(round(blob.sentiment.polarity, 2))
# print(round(blob.sentiment.subjectivity, 2))

# sentences = blob.sentences

# for sentence in sentences:
#     print(sentence)
#     print(sentence.sentiment)
#     print(round(sentence.sentiment.polarity, 2))
#     print(round(sentence.sentiment.subjectivity, 2))

from textblob.sentiments import NaiveBayesAnalyzer

# blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# print(blob.sentiment)

# Language Detection
# print(blob.detect_language())
"""
spanish = blob.translate(to="es")
print(spanish)

# Inflection
from textblob import Word

index = Word("Index")

print(index.pluralize())

cacti = Word("cacti")
print(cacti.singularize())

animals = TextBlob("dog cat fish bird").words

print(animals.pluralize())

word = Word("theyr")

print(word.spellcheck())

print(word.correct())

sentence = TextBlob("Ths sentence has missplled wrds.")
print(sentence.correct())

# Stemming and Lemmatization
from textblob import Word

word1 = Word("studies")
word2 = Word("varieties")

print(word1.lemmatize())
print(word2.lemmatize())


happy = Word("happy")
print(happy.definitions)

for synset in happy.synsets:
    print(synset)
    for lemma in synset.lemmas():
        print(lemma)
        print(lemma.name())

lemmas = happy.synsets[0].lemmas()
print(lemmas)

for lemma in lemmas[0].antonyms():
    print(lemma.name())

"""
import nltk

# nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("english")

# print(stops)

blob = TextBlob("Today is a beautiful day.")

new_list = [word for word in blob.words if word not in stops]
print(blob.words)
print(new_list)