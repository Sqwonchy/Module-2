def single_root_words(root_word: str, *other_words: str):
    same_words =[]
    prime_word = (str(root_word)).lower()
    for words in other_words:
        word = (str(words)).lower()
        chek = word.count(prime_word)
        chek_1 = prime_word.count(word)
        if chek > 0 or chek_1 > 0:
            same_words.append(words)
    return  (same_words)




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)