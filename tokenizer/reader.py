import os
from . import TokenHolder, Token

"""
Allows to read the tokenizer files
"""

def readTokenFile(filePath: str, holder: TokenHolder) -> list[str] | None:
    if not os.path.exists(filePath):
        return None

    with open(filePath, "r") as f: 
        raw = f.read().replace("\n", " ").replace("\t", " ").replace("\0","").split(" ")

        for token in raw:
            holder.tokens[token] = Token(len(holder.tokens), token)

    return holder.tokens