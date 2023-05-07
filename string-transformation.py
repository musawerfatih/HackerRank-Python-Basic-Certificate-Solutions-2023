def transformSentence(sentence):
    words = sentence.split()  # split the sentence into words
    transformed_words = []
    for word in words:
        transformed_word = word[0]  # the first letter remains unchanged
        for i in range(1, len(word)):
            if word[i-1].lower() < word[i].lower():
                transformed_word += word[i].upper()
            else:
                transformed_word += word[i].lower()
        transformed_words.append(transformed_word)
    return ' '.join(transformed_words)
