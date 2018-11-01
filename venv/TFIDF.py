import math
from textblob import TextBlob as tb

# compute term frequency. Count the occurences of a word divided by size of the document
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

# returns the number of documents containing a word
def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

# computes inverse document frequency. Measures how common a word is among all documents in bloblist
def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

# computes tfidf score. Product of tf and idf
def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


doc1 = tb("""Chess is a two-player strategy board game played on a chessboard, "
          "a checkered gameboard with 64 squares arranged in an 8×8 grid.[1] "
          "The game is played by millions of people worldwide. "
          "Chess is believed to have originated in India sometime before the 7th century."
          " The game was derived from the Indian game chaturanga, which is also the "
          "likely ancestor of the Eastern strategy games xiangqi, janggi, and shogi. "
          "Chess reached Europe by the 9th century, due to the Umayyad conquest of Hispania. "
          "The pieces assumed their current powers in Spain in the late 15th century; "
          "the rules were standardized in the 19th century.""")

doc2 = tb("""The Office is an American television sitcom that aired on NBC from March 24, 2005,"
          " to May 16, 2013, lasting nine seasons. It is an adaptation of the original BBC "
          "series of the same name and was adapted for American television by Greg Daniels, "
          "a veteran writer for Saturday Night Live, King of the Hill, and The Simpsons.""")


doc3 = tb("Kobe Bean Bryant (born August 23, 1978) is an American former professional "
          "basketball player. He played his entire 20-year career with the Los Angeles Lakers "
          "of the National Basketball Association (NBA). He entered the NBA directly from "
          "high school and won five NBA championships with the Lakers.")


"""
For each document store the TF-IDF scores in a dictionary mapping word to score
using dict comprehension. Then sort the words by scores and print the top 5
"""
bloblist = [doc1.lower(), doc2.lower(), doc3.lower()]
for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))

    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}

    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for word, score in sorted_words[:5]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))
    print("\n")