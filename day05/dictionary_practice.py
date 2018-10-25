def most_popular_word(words):
    word_counts = {} # Empty dictionary

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    frequent_word = ""
    frequency = 0
    for word in word_counts:
        if word_counts[word] > frequency:
            frequent_word = word
            frequency = word_counts[word]

    return frequent_word

some_words = ['goldfish', 'heron', 'buzz', 'honey', 'heron', 'buzz', 'buzz']
print(most_popular_word(some_words))




















my_name = {
    "j": 1,
    "o": 1,
    "e": 1,
    "l": 1
}

# The letter l appears in my name 2 times.
# for letter in my_name:
#     print("The letter", letter, "appears in my name", my_name[letter], "times.")
