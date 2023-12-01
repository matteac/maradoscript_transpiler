import enum
import tokenize
import io
from typing import List, Tuple

class Token(enum.Enum):
    PRINT = "print"
    STRING = "string"

class Lexer:
    def __init__(self, input: str):
        self.input = input
    def lex(self):
        tokens: List[Tuple[Token, str]] = []  # token, literal
        keywords = set([
            "print",
        ])
        input_stream = io.BytesIO(self.input.encode())
        tokens_gen = tokenize.tokenize(input_stream.readline)
        for token in tokens_gen:
            if token.type == tokenize.STRING:
                string = token.string[1:-1]
                if string.endswith("\\n"):
                    string = string[:-2]
                    string += "\n"
                tokens.append((Token.STRING, string))
            elif token.string in keywords:
                tokens.append((Token.PRINT, token.string))

        return tokens


