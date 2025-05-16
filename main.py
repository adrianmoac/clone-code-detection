from difflibSimilarities.main import main as difflib_main
from astSimilarities.main import main as ast_main 
import os
import argparse

def main():
  parser = argparse.ArgumentParser(description="Compare files for similarity.")
  parser.add_argument("path", help="Relative path to the file.")
  difflibResults = []
  astResults = []

  args = parser.parse_args()
  
  path = './normalizedDataset/'
  dir_list = [f for f in os.listdir(path) if f.endswith('.py')]

  for dir in dir_list:
      # Percentage using difflib
      dlResult = difflib_main(args.path, os.path.join(path, dir))
      difflibResults.append(dlResult)
      #Percentage using AST
      astResult = ast_main(args.path, os.path.join(path, dir))
      astResults.append(astResult)

  difflibResults = sorted(difflibResults, key=lambda d: list(d.values())[0], reverse=True)
  astResults = sorted(astResults, key=lambda d: list(d.values())[0], reverse=True)

  similarityMatrix = []
  
  for res in astResults:
      (file, similarity), = res.items()
      isPlagiarism = similarity >= 60
      similarityMatrix.append([file, similarity, isPlagiarism])

    
  print(difflibResults)
  print(astResults)

if __name__ == "__main__":
  main()