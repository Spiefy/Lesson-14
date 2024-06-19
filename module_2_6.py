def single_root_words(root_word, *other_words):
    same_words = []
    lower_root = root_word.lower()
    lower_tuple = tuple(x.lower() for x in other_words)
    for i in lower_tuple:
        if lower_root in i:
            same_words.append(i)
        elif i in lower_root:
            same_words.append(i)
    return same_words


result1 = single_root_words('rIch', 'Richiest', 'oriChalcum', 'cheers', 'rIchies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
