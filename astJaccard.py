import ast
import argparse

def normalize_ast(tree):
    """Normalize AST to abstract away variable and function names."""
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

def get_node_type_set(tree):
    """Get a set of AST node types from the tree."""
    return {type(node).__name__ for node in ast.walk(tree)}

def load_and_extract_features(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
        norm_tree = normalize_ast(tree)
        return get_node_type_set(norm_tree)
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return set()

def jaccard_similarity(set1, set2):
    """Compute Jaccard similarity between two sets."""
    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union) if union else 1.0

def main(path1, path2):
    features1 = load_and_extract_features(path1)
    features2 = load_and_extract_features(path2)

    similarity = jaccard_similarity(features1, features2)
    print(f"Jaccard similarity: {round(similarity * 100, 2)}%")
    return {path2: round(similarity * 100, 2)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file1')
    parser.add_argument('file2')
    args = parser.parse_args()
    main(args.file1, args.file2)
