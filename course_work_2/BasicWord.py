class BasicWord(object):
    '''
    Word with subwords.
    check_word(word): check input words
    words_count: return number of words

    >>> w = BasicWord("набор", ["бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"])
    >>> w.word == "набор"
    True
    >>> w.subwords == ["бар", "бон", "бор", "раб", "бра", "боа", "нора", "роба", "барон"]
    True
    >>> w.check_word("бар") == True
    True
    >>> w.words_count() == 9
    True
    '''

    def __init__(self, word: str, subwords: [str]):
        self.word = word
        self.subwords = subwords

    def check_word(self, word):
        return word in self.subwords

    def words_count(self):
        return len(self.subwords)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
