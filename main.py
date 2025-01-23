import tokenizer

# Tokenizer test

def main():
    tokens = ["Hello", "are", "you", "how"]
    holder = tokenizer.TokenHolder()

    for index, token in enumerate(tokens):
        holder.tokens[token] = index

    text = "Hello how are you?"

    tt = tokenizer.tokenize(holder, text)

    for token in tt:
        print(f"Token of type {str(token.type)}")

main()