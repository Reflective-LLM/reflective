import tokenizer

# Tokenizer test

def main():
    holder = tokenizer.TokenHolder()
    tokenizer.readTokenFile("data/tokens", holder)

    text = "Hello how are you?"

    tt = holder.tokenize(text)

    for token in tt:
        print(f"Token of type {str(token.type)}")

main()