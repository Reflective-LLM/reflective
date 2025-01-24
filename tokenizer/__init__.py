"""
Main file of the tokenizer
"""

from .tokens import TokenHolder, Token

def tokenize(holder: TokenHolder, text: str) -> list[Token]:
    tokens: list[Token] = []
    splits: list[str] = text.split(" ")

    for word in splits:
        buff: str = ""
        pos: int = 0

        while pos < len(word):
            found = False
            for entry in holder.tokens:
                if word[pos:] == entry and len(word[pos:]) > len(buff):
                    buff = word[pos:]
                    pos += 1
                    found = True
                    break

            if not found:
                pos += 1
        
        
        if not buff == "":
            tokens.append(Token(holder.tokens[buff], buff))
            print(f"Token detected: id: {str(holder.tokens[buff])} with raw {buff}")

    return tokens

from .reader import readTokenFile