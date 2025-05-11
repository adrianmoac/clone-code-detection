from . import diff

def main(path1, path2):
    return {path2: diff.getDiff(path1, path2)}