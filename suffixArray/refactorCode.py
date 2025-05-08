import tokenize
import token as TK
from io import BytesIO

def refactorCode(file) -> str:
    """
    Removes spaces, comments, and changes all non-reserved words to a default name.
    """
    # Reserved words
    keywords = [
        'False', 'None', 'True', '_', 'and', 'as', 'assert', 'async', 
        'await', 'break', 'case', 'class', 'continue', 'def', 'del', 
        'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
        'if', 'import', 'in', 'is', 'lambda', 'match', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'type', 'try', 'while', 
        'with', 'yield', 'input', 'split', 'map', 'print'
    ]

    newTokens = []

    cleanedLines = []
    insideMultilineComment = False
    # Looks for comments in the code in the form of ' # ' and ' """ '
    for line in file.splitlines():
        if '"""' in line or "'''" in line:
            insideMultilineComment = not insideMultilineComment
            continue  
        elif insideMultilineComment:
            continue 
        elif line.strip().startswith('#'):
            continue 
        else:
            cleanedLine = ' '.join(line.strip().split())
            cleanedLines.append(cleanedLine)

    # Join the cleaned lines without newlines
    fileWithoutSpaces = ' '.join(cleanedLines)

    # Get tokens
    tokens = tokenize.tokenize(BytesIO(fileWithoutSpaces.encode('utf-8')).readline)

    idNumber = 0
    for token in tokens:
        # Find non-reserved words and change their names to a default name
        if token.type == TK.NAME and token.string not in keywords:
            new_token = tokenize.TokenInfo(token.type, 'id' + str(idNumber), token.start, token.end, token.line)
            newTokens.append(new_token)
            idNumber += 1
        else:
            newTokens.append(token)

    result = tokenize.untokenize(newTokens)
    # Return the result as a string without newlines
    return result.decode('utf-8').replace('\n', '')
