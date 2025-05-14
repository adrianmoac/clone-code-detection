import tokenize
import token as TK
from io import BytesIO
import re  
import os

def refactorCode(originalCode) -> str:
    """
    Removes spaces, comments, and changes all non-reserved words to a default name, while preserving indentation.
    """
    keywords = set([
        'False', 'None', 'True', '_', 'and', 'as', 'assert', 'async', 
        'await', 'break', 'case', 'class', 'continue', 'def', 'del', 
        'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
        'if', 'import', 'in', 'is', 'lambda', 'match', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'type', 'try', 'while', 
        'with', 'yield', 'input', 'split', 'map', 'print'
    ])

    var_mapping = {}
    id_counter = 0
    newTokens = []

    lines = originalCode.splitlines()

    fileWithoutSpaces = '\n'.join(lines)
    fileWithoutSpaces = re.sub(r'\s*([+\-*/%&|^=<>!])\s*', r'\1', fileWithoutSpaces)

    tokens = tokenize.tokenize(BytesIO(fileWithoutSpaces.encode('utf-8')).readline)

    for token in tokens:
        if token.type == TK.STRING:
            new_string = token.string.replace("'", '"') 
            new_token = tokenize.TokenInfo(token.type, new_string, token.start, token.end, token.line)
            newTokens.append(new_token)
        elif token.type == TK.NAME and token.string not in keywords:
            if token.string not in var_mapping:
                var_mapping[token.string] = f"id{id_counter}"
                id_counter += 1
            replacement = var_mapping[token.string]
            new_token = tokenize.TokenInfo(token.type, replacement, token.start, token.end, token.line)
            newTokens.append(new_token)
        else:
            newTokens.append(token)

    result = tokenize.untokenize(newTokens)
    return result.decode('utf-8')


def refactor_file(input_path: str, output_path: str):
    with open(input_path, 'r', encoding='utf-8') as f:
        original_code = f.read()

    refactored_code = refactorCode(original_code)

    outputDir = "./normalizedDataset"
    os.makedirs(outputDir, exist_ok=True)
    outputPath = os.path.join(outputDir, output_path)

    with open(outputPath, "w", encoding='utf-8') as f:
        f.write(refactored_code)


def main():
    path = './dataset/'
    dir_list = [f for f in os.listdir(path) if f.endswith('.py')]
    print("Python files in '", path, "' :")
    print(dir_list)

    for dir in dir_list:
        refactor_file(os.path.join(path, dir), dir)


if __name__ == "__main__":
    main()
