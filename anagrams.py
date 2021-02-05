def anagrams(word, words):
    """returns all letter combimations met in list"""
    return [_ for _ in words if sorted(list(_)) == sorted(list(word))]
    # return [f'{_}, {word}' for _ in words if _ != word and list(_) == list(word)]
    # return [_, word for _ in words if list(_) == list(word) else None]


test1 = 'abba'
test2 = ['aabb', 'abcd', 'bbaa', 'dada']  # ['carer', 'racer']
print(anagrams(test1, test2))
