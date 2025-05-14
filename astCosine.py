import ast
import argparse
from collections import Counter
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def normalize_ast(tree):
    # (Same normalize_ast function as before)
    class Normalizer(ast.NodeTransformer):
        def visit_Name(self, node):
            return ast.copy_location(ast.Name(id='var', ctx=node.ctx), node)
        def visit_arg(self, node):
            node.arg = 'arg'
            return node
        def visit_FunctionDef(self, node):
            node.name = 'func'
            self.generic_visit(node)
            return node
    return Normalizer().visit(tree)

def load_and_extract_features(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
        norm_tree = normalize_ast(tree)
        # Simple feature: Count of different node types
        node_counts = Counter()
        for node in ast.walk(norm_tree):
            node_counts[type(node).__name__] += 1
        return np.array(list(node_counts.values()))
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return None

def main(path1, path2):
    features1 = load_and_extract_features(path1)
    features2 = load_and_extract_features(path2)

    if features1 is None or features2 is None:
        return {path2: 0.0}

    # Ensure both feature vectors have the same length (fill with 0 if needed)
    all_keys = set(Counter(ast.walk(normalize_ast(ast.parse(open(path1).read())))).keys()) | set(Counter(ast.walk(normalize_ast(ast.parse(open(path2).read())))).keys())
    features1_dict = Counter(ast.walk(normalize_ast(ast.parse(open(path1).read()))))
    features2_dict = Counter(ast.walk(normalize_ast(ast.parse(open(path2).read()))))

    vector1 = np.array([features1_dict.get(key, 0) for key in all_keys])
    vector2 = np.array([features2_dict.get(key, 0) for key in all_keys])


    # Calculate cosine similarity
    if np.linalg.norm(vector1) == 0 or np.linalg.norm(vector2) == 0:
        similarity = 0.0
    else:
        similarity = cosine_similarity(vector1.reshape(1, -1), vector2.reshape(1, -1))[0][0]

    return {path2: round(similarity * 100, 2)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compare two Python files for similarity using ASTs and a simple ML approach.")
    parser.add_argument("path1", help="Path to the first Python file.")
    parser.add_argument("path2", help="Path to the second Python file.")
    args = parser.parse_args()
    result = main(args.path1, args.path2)
    print(result)