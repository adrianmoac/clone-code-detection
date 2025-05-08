import longestSuffixes 
import refactorCode
import createReport

def similarity_from_lcp_list(lcp_list):
    return sum(len(prefix) for prefix in lcp_list)

def calculateSimilarity(path1, path2, preprocessCode):
  """
  Get similarity from both codes by refactoring and comparing suffixes
  """
  file1 = open(path1, 'r', encoding='utf-8').read()
  file2 = open(path2, 'r', encoding='utf-8').read()

  if preprocessCode == True:
    file1 = refactorCode.refactorCode(file1)
    file2 = refactorCode.refactorCode(file2)

  # Get all common substrings
  allCommon = longestSuffixes.findAllLongestCommonSuffixes(file1, file2)

  # Remove duplicates and nested substrings
  maxLcps = longestSuffixes.removeNestedSuffixes(allCommon)

  # Calculate similarity with the substrings
  similarity = (2 * similarity_from_lcp_list(maxLcps)) / (len(file1) + len(file2))
  similarity = round(similarity * 100, 2)
  createReport.getReport(maxLcps, similarity)  