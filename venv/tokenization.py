import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize, punkt
# nltk.download('punkt_tab')

# Sentence to use
corpus = """word_tokenize: Return a tokenized copy of text, using NLTK's recommended word tokenizer 
(currently an improved .TreebankWordTokenizer along with .PunktSentenceTokenizer for the specified language)."""

word_token_document = word_tokenize(corpus)
print(word_token_document)

wordpunct_token_document = wordpunct_tokenize(corpus)
print(wordpunct_token_document)

sent_token_document = sent_tokenize(corpus)
print(sent_token_document)



