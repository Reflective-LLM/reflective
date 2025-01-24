class Token:
    def __init__(self, t: int, word: str):
        self.type = t
        self.word = word

class TokenHolder:
    def __init__(self):
        self.tokens: dict(str, int) = {}
    
    def tokenize(text: str) -> list[Token]:
        tokens: list[Token] = []
        splits: list[str] = text.split(" ")
        for word in splits:
            buff: str = ""
            pos: int = 0

            while pos < len(word):
                found = False
                for entry in self.tokens:
                    if word[pos:] == entry and len(word[pos:]) > len(buff):
                        buff = word[pos:]
                        pos += 1
                        found = True
                        break

                if not found:
                    pos += 1
            
            
            if not buff == "":
                tokens.append(Token(self.tokens[buff], buff))

        return tokens
        

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