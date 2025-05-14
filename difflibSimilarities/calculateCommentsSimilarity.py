def getSimilarity(commentsCode1, commentsCode2):
    set1 = set(commentsCode1)
    set2 = set(commentsCode2)
    
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    
    if not union:
        return 1.0  # if both are empty, consider them 100% similar
    return round(len(intersection) / len(union) * 100, 2)
