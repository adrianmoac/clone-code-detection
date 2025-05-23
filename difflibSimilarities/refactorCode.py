import tokenize
import token as TK
from io import BytesIO
import re  

def refactorCode(originalCode) -> str:
    """
    Removes spaces, comments and changes all not reserved words for a default name.
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


    cleanedLines = []
    insideMultilineComment = False
    for line in originalCode.splitlines():
        if '"""' in line or "'''" in line:
            insideMultilineComment = not insideMultilineComment
            continue  
        elif insideMultilineComment or line.strip().startswith('#'):
            continue 
        else:
            cleanedLine = ' '.join(line.strip().split())
            if cleanedLine:  
                cleanedLines.append(cleanedLine)

    fileWithoutSpaces = '\n'.join(cleanedLines)
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