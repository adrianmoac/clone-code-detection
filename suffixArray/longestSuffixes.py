def buildSuffixArray(text):
  """
  Given the received text, get all the suffixes
  """
  return sorted(range(len(text)), key=lambda i: text[i:])

def commonSuffixLen(s1, s2):
  """
  Get the length of the received prefixes
  """
  i = 0
  while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
      i += 1
  return i

def findAllLongestCommonSuffixes(text1, text2):
  """
  Get and return all the longest prefixes
  """
  combined = text1 + '#' + text2 + '$'
  suffix_array = buildSuffixArray(combined)

  lcpList = []

  for i in range(1, len(suffix_array)):
    s1 = suffix_array[i - 1]
    s2 = suffix_array[i]

    # Only consider suffixes from different input strings
    if (s1 < len(text1) and s2 > len(text1)) or (s2 < len(text1) and s1 > len(text1)):
      cpLen = commonSuffixLen(combined[s1:], combined[s2:])
      cp = combined[s1:s1 + cpLen]
      if cpLen > 0:
        lcpList.append(cp)

  return lcpList

def removeNestedSuffixes(lcpList):
  """
  Keep only the longest substrings that are not included in others
  """
  # Sort by descending length
  lcpList = sorted(set(lcpList), key=lambda x: -len(x))

  result = []
  for i, s in enumerate(lcpList):
    if not any(s != other and s in other for other in lcpList[:i]):
      result.append(s)
  return result