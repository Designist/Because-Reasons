from textblob import TextBlob

text = '''I am going to sleep because reasons. I am going to sleep because great reasons.'''

blob = TextBlob(text)

for sentence in blob.noun_phrases:
    print(sentence)