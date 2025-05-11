def getSimilarity(shortestFileLength, diffString) -> float:
  """
  From the received diff string, count all the differences and return the percentage of similarities.
  """
  totalCharDifferences = 0

  diffList = "".join(diffString).splitlines()

  i = 0
  while i < len(diffList):
      line = diffList[i]
      if i + 1 < len(diffList) and line.startswith('-') and not diffList[i + 1].startswith('?'):
         totalCharDifferences += len(line)
      # Lines starting with '?' mark character-level differences
      elif line.startswith('?'):
          # Count the number of '^' and '-' characters which indicate changes
        for c in line:
            if c == '^' or c == '-':
                totalCharDifferences += 1
      i += 1

  # Get the percentage of similarities
  totalSimilaritiesPercentage = (shortestFileLength - totalCharDifferences) * 100 / shortestFileLength
  if totalSimilaritiesPercentage < 0:
     totalSimilaritiesPercentage = 0.0
  elif totalSimilaritiesPercentage > 100:
     totalSimilaritiesPercentage = 100
  # Trunc it two decimals
  totalSimilaritiesPercentage = round(totalSimilaritiesPercentage, 2)

  return totalSimilaritiesPercentage