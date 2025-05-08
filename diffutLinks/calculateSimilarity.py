import createReport 

def getSimilarity(shortestFileLength, diffString, isLeftFile) -> float:
  """
  From the received diff string, count all the differences and return the percentage of similarities.
  """
  totalCharEqualities = 0
  # Format the diff to a list to read it
  diffList = "".join(diffString).splitlines()

  for i in range(len(diffList) - 1):
    line = diffList[i]
    next_line = diffList[i + 1]
    # If next line does not start with ?, it means that the whole line changes
    if not next_line.startswith('?'):
      # Get only the differences from the smaller file
      if isLeftFile and line.startswith('-'):
        for char in line:
          if char != " ":
            totalCharEqualities += 1
      elif not isLeftFile and line.startswith('+'):
        for char in line:
          if char != " ":
            totalCharEqualities += 1
    # If current line starts with ?, it means that only some characters change
    if line.startswith('?'):
      for char in line:
        if char in ['-', '^']:
          totalCharEqualities += 1

  # Get the percentage of similarities
  totalSimilaritiesPercentage = (shortestFileLength - totalCharEqualities) * 100 / shortestFileLength
  # Trunc it two decimals
  totalSimilaritiesPercentage = round(totalSimilaritiesPercentage, 2)
  createReport.getReport(diffList, totalSimilaritiesPercentage)