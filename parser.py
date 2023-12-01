from lexer import Lexer, Token

class Parser:
    def __init__(self, input: str):
        self.input = input
    def parse(self) -> str:
        lexer = Lexer(self.input)
        tokens = lexer.lex()
        previous_token = None
        current_token = None
        output = ""
        for token in tokens:
            previous_token = current_token
            current_token = token
            if previous_token is None:
                continue
            if previous_token[0] == Token.PRINT and current_token[0] == Token.PRINT:
                print(f"ERROR: {previous_token} {current_token}")
                exit(1)
            if previous_token[0] == Token.PRINT and current_token[0] == Token.STRING:
                string = current_token[1]
                for char in string:
                    ascii_code = ord(char)
                    output += "m"*ascii_code
                    output += "👍e"
        return output
