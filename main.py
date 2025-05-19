from difflibSimilarities.main import main as difflib_main
from astSimilarities.main import main as ast_main 
import os
import sys

def main(filePath):
  difflibResults = []
  astResults = []

  if getattr(sys, 'frozen', False):
      base_dir = sys._MEIPASS
  else:
      base_dir = os.path.dirname(os.path.abspath(__file__))
  path = os.path.join(base_dir, 'normalizedDataset')

  if not os.path.exists(path):
      raise FileNotFoundError(f"Directory not found: {path}")
  dir_list = [f for f in os.listdir(path) if f.endswith('.py')]

  for dir in dir_list:
      # Percentage using difflib
      dlResult = difflib_main(filePath, os.path.join(path, dir))
      difflibResults.append(dlResult)
      #Percentage using AST
      astResult = ast_main(filePath, os.path.join(path, dir))
      astResults.append(astResult)

  difflibResults = sorted(difflibResults, key=lambda d: list(d.values())[0], reverse=True)
  astResults = sorted(astResults, key=lambda d: list(d.values())[0], reverse=True)

  similarityMatrix = []
  
  for res in astResults:
      (file, similarity), = res.items()
      isPlagiarism = similarity >= 60
      similarityMatrix.append([file, similarity, isPlagiarism])

  return [difflibResults, astResults]