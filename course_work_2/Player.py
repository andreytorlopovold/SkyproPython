class Player(object):
    '''
    Player object contain user words
    check words, add word and get words count
    >>> p = Player('User')
    >>> p.words == set([])
    True
    >>> p.add("Foo")
    >>> p.words == {'Foo'}
    True
    >>> p.check_word('Foo') == True
    True
    >>> p.check_word('Bar') == True
    False
    '''

    def __init__(self, user_name):
        self.user_name = user_name
        self.words = set([])

    def words_count(self):
        return len(self.words)

    def add(self, word):
        self.words.add(word)

    def check_word(self, word):
        return word in self.words


if __name__ == "__main__":
    import doctest

    doctest.testmod()
