import difflib
import refactorCode
import calculateSimilarity


def getDiff(file1, file2):
  """
  Calculate the similarities of two received files by using the original files or preprocess them to find more similarities. 
  """
  f1 = open(file1).read()
  f2 = open(file2).read()
  
  lines1 = refactorCode.refactorCode(file1).splitlines(keepends=True)
  lines2 = refactorCode.refactorCode(file2).splitlines(keepends=True)

  # Get similarities
  diff = list(difflib.ndiff(lines1, lines2))

  # Find which file is smaller so it can be used to calculate similarities
  shortestFileLength = None
  isLeftFile = False
  if(len(f1) < len(f2)):
    shortestFileLength = len(f1)
    isLeftFile = True
  else:
    shortestFileLength = len(f2)
  calculateSimilarity.getSimilarity(shortestFileLength, diff, isLeftFile)
