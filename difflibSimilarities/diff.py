import difflib
from . import refactorCode
from . import calculateSimilarity

def countTotalCharacters(lines):
  """
  Count the total number of characters in the lines of code.
  """
  total_characters = 0
  for line in lines:
      total_characters += len(line)
  return total_characters

def getDiff(file1, file2):
  """
  Calculate the similarities of two received files by using the original files or preprocess them to find more similarities. 
  """
  
  f1 = open(file1, 'r', encoding='utf-8', errors='ignore').read()
  f2 = open(file2, 'r', encoding='utf-8', errors='ignore').read()

  lines1 = refactorCode.refactorCode(f1).splitlines(keepends=True)
  lines2 = [line.lstrip() for line in f2.splitlines(keepends=True)]

  # Get similarities
  diff = list(difflib.ndiff(lines1, lines2))

  lines1Length = countTotalCharacters(lines1)
  lines2Length = countTotalCharacters(lines2)

  # Find which file is smaller so it can be used to calculate similarity percentage
  shortestFileLength = None

  if(lines1Length < lines2Length):
    shortestFileLength = lines1Length
  else:
    shortestFileLength = lines2Length
  
  return calculateSimilarity.getSimilarity(shortestFileLength, diff)
