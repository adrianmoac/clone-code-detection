import ast
import difflib
import argparse
import sys

class Normalizer(ast.NodeTransformer):
    def visit_Name(self, node):
        return ast.copy_location(ast.Name(id='var', ctx=node.ctx), node)

    def visit_arg(self, node):
        node.arg = 'arg'
        return node

    def visit_FunctionDef(self, node):
        # Keep function name for precision
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        # Keep class name for precision
        self.generic_visit(node)
        return node

    # Do NOT normalize constants here – keep real literals

def normalize_ast(tree):
    return Normalizer().visit(tree)

def load_and_normalize_ast(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
        norm_tree = normalize_ast(tree)
        ast.fix_missing_locations(norm_tree)

        try:
            from ast import unparse
            normalized_code = unparse(norm_tree)
        except ImportError:
            normalized_code = ast.dump(norm_tree)

        return normalized_code
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}", file=sys.stderr)
        return ""

def main():
    parser = argparse.ArgumentParser(description="Compare two Python files by normalized AST similarity.")
    parser.add_argument("file1", help="Path to the first Python file")
    parser.add_argument("file2", help="Path to the second Python file")
    args = parser.parse_args()

    dump1 = load_and_normalize_ast(args.file1)
    dump2 = load_and_normalize_ast(args.file2)

    similarity = difflib.SequenceMatcher(None, dump1, dump2).ratio()
    print(f"Similarity: {similarity:.2%}")

if __name__ == '__main__':
    main()
