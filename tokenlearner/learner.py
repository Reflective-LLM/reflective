from tokenizer import Token, TokenHolder

def learnFromText(holder: TokenHolder, path: str):
    with open(path, "r") as f:
        text = f.read()
    
    # Ensures that the signs are kept
    text = text.replace("?", "?.").replace("!", "!.")
    
    sequences = text.split(".")

    for seq in sequences:
        for word in seq.split(" "):
            if not word == "" and word.isalpha():
                if not word in holder.tokens:
                    holder.tokens[word] = len(holder.tokens)