def getComments(originalCode):
  extractedComments = []
  insideMultilineComment = False
  
  for line in originalCode.splitlines():
      stripped = line.strip()
      
      stripped = stripped.replace(' ', '')

      # Handle multiline comments / docstrings
      if ('"""' in stripped or "'''" in stripped):
          insideMultilineComment = not insideMultilineComment
          continue

      if insideMultilineComment:
          if stripped:
              extractedComments.append(stripped.lower())
          continue

      # Handle single-line comments
      if stripped.startswith('#'):
          extractedComments.append(stripped.lower())
          continue

  return extractedComments