import createReport 

def getSimilarity(shortest_len, diff, is_left_file) -> float:
    """
    Calculates similarity based on character equality, ignoring diff guide lines.
    """
    matches = 0
    total = 0

    for line in diff:
        if line.startswith("  ") or line.startswith('-') or line.startswith('+'):
            content = line[2:]
            total += len(content)
            if line.startswith("  "):
                matches += len(content)

    similarity = (matches / total) * 100 if total > 0 else 100.0
    similarity = round(similarity, 2)

    from createReport import getReport
    common_lines = [line for line in diff if line.startswith("  ")]
    getReport(common_lines, similarity)
    return similarity
