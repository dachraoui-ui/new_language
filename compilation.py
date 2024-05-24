import re
import sys

class Token:
    def __init__(self, lexeme, token):
        self.lexeme = lexeme
        self.token = token

    def __str__(self):
        return f"<{self.token}, {self.lexeme}>"

def tokenize(input_text):
    token_patterns = {
        "PROG_START": r"@PROG",
        "PROG_END": r"PROG@",
        "DECL_START": r"@DECL",
        "DECL_END": r"DECL@",
        "CORPS_START": r"@CORPS",
        "CORPS_END": r"CORPS@",
        "ECRIRE": r"ECRIRE",
        "FOR": r"FOR",
        "ENTIER": r"ENTIER",
        "REEL": r"REEL",
        "CARACTERE": r"CARACTERE",
        "TABLEAU": r"TABLEAU",
        "CHAINE": r"CHAINE",
        "INCREMENT": r"\+\+",
        "AFFECT": r":=",
        "ADD": r"ADD",
        "SOUS": r"SOUS",
        "MULT": r"MULT",
        "OPREL": r"<=|>=|<>|==|>|<",
        "IDENT": r"%\d+",
        "NBREEL": r"\d+\.\d+",
        "NBENTIER": r"\d+",
        "STRING": r"\"[^\"]*\"",
        "LPAREN": r"\(",
        "RPAREN": r"\)",
        "LBRACKET": r"\[",
        "RBRACKET": r"\]",
        "COMMA": r",",
        "SEMICOLON": r";",
    }

    patterns = '|'.join(f"(?P<{name}>{pattern})" for name, pattern in token_patterns.items())
    compiled_pattern = re.compile(patterns)

    tokens = []
    for match in compiled_pattern.finditer(input_text):
        for name, _ in token_patterns.items():
            if match.group(name):
                tokens.append(Token(match.group(name), name))
                break
    return tokens

def main():
    if len(sys.argv) != 2:
        print("Usage: python LexicalAnalyzer.py <source-file>")
        sys.exit(1)

    source_file_path = sys.argv[1]
    print(f"Reading source file from: {source_file_path}")

    try:
        with open(source_file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Source file not found: {source_file_path}")
        sys.exit(1)
    except IOError as e:
        print(f"Error reading source file: {e}")
        sys.exit(1)

    print("Source file read successfully. Starting tokenization...")

    tokens = tokenize(code)
    for token in tokens:
        print(token)

    try:
        with open("output2.lex", 'w', encoding='utf-8') as file:
            for token in tokens:
                file.write(str(token) + '\n')
    except IOError as e:
        print(f"Error writing to output file: {e}")

    print("Tokenization completed. Tokens written to output.lex.")

if __name__ == "__main__":
    main()
