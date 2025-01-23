"""
Main file of the tokenizer
"""

# Holds every known token type
class TokenHolder:
    def __init__(self):
        self.tokens: list[str] = []

class Token:
    def __init__(self, t: int, word: str):
        self.type = t
        self.word = word

def tokenize(holder: TokenHolder, text: str) -> list[Token]:
    tokens: list[Token] = []
    splits: list[str] = text.split(" ")

    for word in splits:
        buff: str = ""

        for c in word:
            buff += c
            
            if len(buff) >= 2:
                if buff in holder.tokens: 
                    tokens.append(Token(holder.tokens[buff], buff))
                    buff = ""
    
    return tokens