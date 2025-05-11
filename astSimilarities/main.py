import ast
import difflib
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

def load_and_normalize_ast(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        source = f.read()
    try:
        tree = ast.parse(source)
        norm_tree = normalize_ast(tree)
        return ast.dump(tree)
    except SyntaxError as e:
        print(f"Syntax error in {filepath}: {e}")
        return ""

def main(path1, path2):
    dump1 = load_and_normalize_ast(path1)
    dump2 = load_and_normalize_ast(path2)

    similarity = difflib.SequenceMatcher(None, dump1, dump2).ratio()
    return {path2: round(similarity * 100, 2)}

if __name__ == '__main__':
    main()
