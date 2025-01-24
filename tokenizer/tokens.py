class Token:
    def __init__(self, t: int, word: str):
        self.type = t
        self.word = word

class TokenHolder:
    def __init__(self):
        self.tokens: dict(str, int) = {}
