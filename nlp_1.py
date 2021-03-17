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

# spanish = blob.translate(to="es")
# print(spanish)

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
