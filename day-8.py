import string

def count_words(text):
    translator =str.maketrans('','',string.punctuation)
    cleaned_text=text.translate(translator).lower()
    words=cleaned_text.split()
    word_counts = {}
    for word in words:
        word_counts[word]=word_counts.get(word,0)+1
    return word_counts

# Example function calls
print(count_words("Hello world! Hello again, world."))  # Should return {"hello": 2, "world": 2, "again": 1}
print(count_words("Unique words only once."))  # Should return {"unique": 1, "words": 1, "only": 1, "once": 1}