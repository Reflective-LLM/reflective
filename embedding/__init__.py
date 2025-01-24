import random
import tokenizer
from math import sin, cos

class Embedder:
    def __init__(self, *, vocab_size: int = 50257, embed_dim: int = 768):
        self.vocab_size = vocab_size
        self.embed_dim = embed_dim
        self.embedding_matrix = [
            [random.uniform(-1, 1) for _ in range(embed_dim)]
            for _ in range(vocab_size)
        ]
        self.token_to_id = tokenizer.tokens.TokenHolder().tokens
        self.id_to_token = {v: k for k, v in self.token_to_id.items()}

    def get_embedding(self, token: tokenizer.Token) -> list[float] | None:
        token_id = self.token_to_id(token.word, -1)
        if token_id == -1:
            return None
        return self.embedding_matrix[token_id]

    def get_seq_embedding(self, tokens: list[tokenizer.Token]) -> list[list[float]] | None:
        return [self.get_embedding(t) for t in tokens]

    def pos_encoding(self, seq_len: int) -> list[float | int]:
        position_encoding = []
        for pos in range(seq_len):
            pos_enc = []
            for i in range(self.embed_dim):
                pos_enc.append(sin(pos / 10000 ** (2 * i / self.embed_dim))) if i % 2 == 0 else pos_enc.append(cos(pos / 10000 ** (2 * i / self.embed_dim)))
            position_encoding.append(pos_enc)
        return position_encoding
    
    def combine_embedddings(self, tokens) -> list[list[tokenizer.Token]]:
        tkn_embeddings = self.get_seq_embedding(tokens)
        pos_encodings = self.pos_encoding(len(tokens))

        return [
            [t+p for t,p in zip(tkn_emb, pos_enc)]
            for tkn_emb, pos_enc in zip(tkn_embeddings, pos_encodings)
        ]
