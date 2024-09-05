from collections import Counter
class WordsFrequency:
    def __init__(self, book):
        self.cnt = Counter(book)

    def get(self, word: str) -> int:
        return self.cnt[word]

