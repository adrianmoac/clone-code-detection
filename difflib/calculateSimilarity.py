import createReport 

def getSimilarity(shortestFileLength, diffString) -> float:
  """
  From the received diff string, count all the differences and return the percentage of similarities.
  """
  totalCharDifferences = 0

  diffList = "".join(diffString).splitlines()

  i = 0
  while i < len(diffList):
      line = diffList[i]
      # Lines starting with '?' mark character-level differences
      if line.startswith('?'):
          # Count the number of '^' and '-' characters which indicate changes
        for c in line:
            if c == '^' or c == '-':
                totalCharDifferences += 1
      i += 1

  # Get the percentage of similarities
  totalSimilaritiesPercentage = (shortestFileLength - totalCharDifferences) * 100 / shortestFileLength
  # Trunc it two decimals
  totalSimilaritiesPercentage = round(totalSimilaritiesPercentage, 2)
  createReport.getReport(diffList, totalSimilaritiesPercentage)