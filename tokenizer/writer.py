from . import TokenHolder, Token

# Writes the TokenHolder into a data file.
def writeTokenFile(filePath: str, holder: TokenHolder):
    with open(filePath, "w") as f:
        for word in holder.tokens:
            f.write(f"{word} ")