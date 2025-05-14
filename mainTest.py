# -*- coding : utf -8 -*-
""" Module for AST program comparison .

This module implements functions for comparing . py files.
It uses abstract syntax trees from the built in module ’ ast ’. """
import ast
from _ast import *

from munkres import Munkres


def compare_ASTs ( ast_a : AST , ast_b : AST , reorder_depth : int) -> int: 
    """ Compare two ASTs corresponding to python programs.
    Args:
    ast_a : The first program AST to compare . ast_b : The first program AST to compare .
    reorder_depth : The maximum children reorder depth for better performance .

    Returns:
    True if the ASTs are equivalent , otherwise False .
    """
    children_a = list( ast. iter_child_nodes ( ast_a )) 
    children_b = list( ast. iter_child_nodes ( ast_b ))

    if (( type ( ast_a ) == type ( ast_b )) and len ( list( children_a )) == 0 and len ( list( children_b )) == 0):
      return  1
    
    if (( type ( ast_a ) != type ( ast_b )) or ( len ( children_a ) != len ( children_b ))):
      return  0
  
    if reorder_depth == 0:
      match_index  = sum ( map ( lambda  pairs:  compare_ASTs (
      pairs [0], pairs [1], reorder_depth ),
      zip ( children_a , children_b )))
      return match_index + 1

    elif reorder_depth > 0:
      match_index = reorder_children_compare (
      ast_a , ast_b , reorder_depth - 1)
      return match_index + 1

    return  0


from munkres import Munkres
import ast

def reorder_children_compare(ast_a: ast.AST, ast_b: ast.AST, reorder_depth: int) -> int:
    """
    Reorders child nodes and compares them.

    Args:
        ast_a: The first AST for child comparison.
        ast_b: The second AST for child comparison.
        reorder_depth: The maximum children reorder depth for better performance.

    Returns:
        An integer representing the best match score between reordered child nodes.
    """
    comparison_matrix = []
    cost_matrix = []
    best_match_value = 0

    children_a = list(ast.iter_child_nodes(ast_a))
    children_b = list(ast.iter_child_nodes(ast_b))

    if len(children_a) <= 1 or len(children_b) <= 1:
        for child_a in children_a:
            for child_b in children_b:
                best_match_value += compare_ASTs(child_a, child_b, reorder_depth)
    else:
        for child_a in children_a:
            row = []
            cost_row = []
            for child_b in children_b:
                similarity = compare_ASTs(child_a, child_b, reorder_depth)
                row.append(similarity)
                cost_row.append(10000000 - similarity)
            comparison_matrix.append(row)
            cost_matrix.append(cost_row)

        m = Munkres()
        indices = m.compute(cost_matrix)

        for row, col in indices:
            best_match_value += comparison_matrix[row][col]

    return best_match_value



from munkres import Munkres

def compare_subtrees(sig_subtrees_p1: list, sig_subtrees_p2: list, reorder_depth: int) -> tuple:
    """
    Compare two significant subtree lists reordering up to a certain depth.

    Args:
        sig_subtrees_p1: The first significant AST list for comparison.
        sig_subtrees_p2: The second significant AST list for comparison.
        reorder_depth: The maximum children reorder depth for better performance.

    Returns:
        A tuple with the ratio of matching to non-matching nodes of the
        significant subtrees, and a list with the best matching of subtrees.
    """
    comparison_matrix = []
    cost_matrix = []
    best_match = []
    best_match_value = 0
    best_match_weight = 0

    children_a = sig_subtrees_p1.copy()
    children_b = sig_subtrees_p2.copy()

    if len(children_a) <= 1 or len(children_b) <= 1:
        for child_a in children_a:
            best_match.append(child_a)
            for child_b in children_b:
                best_match_value += compare_ASTs(child_a, child_b, reorder_depth)
                best_match.append(child_b)
    else:
        for child_a in children_a:
            row = []
            cost_row = []
            for child_b in children_b:
                similarity = compare_ASTs(child_a, child_b, reorder_depth)
                row.append(similarity)
                cost_row.append(10000000 - similarity)
            comparison_matrix.append(row)
            cost_matrix.append(cost_row)

        m = Munkres()
        indices = m.compute(cost_matrix)

        for row , col in indices:
          best_match_weight += apply_weights_to_subtrees_mult(comparison_matrix [row][col],  sig_subtrees_p1 [row],sig_subtrees_p2 [col])
          best_match  +=  [sig_subtrees_p1 [ row ],  sig_subtrees_p2 [ col ]]

    all_subtrees_weight = (sum(map( lambda tree : apply_weights_to_subtrees ( get_num_nodes ( tree ), tree ), sig_subtrees_p1 ))
      + sum ( map ( lambda tree : apply_weights_to_subtrees ( get_num_nodes ( tree ), tree ), sig_subtrees_p2 )))

    similarity = 2 * best_match_weight / all_subtrees_weight

    return round ( similarity , 4), best_match

def	get_significant_subtrees ( root: AST) -> list:
    """ Find the significant subtrees of an AST.
    
    Args:
    root: The root of the main AST.
    
    Returns:
    A list with all the significant subtrees of root.
    """
    significant_subtrees = []
    for node in ast. walk(root):
      if is_significant(node):
        significant_subtrees.append(node)
    return significant_subtrees

	
def	is_significant ( root: AST) -> bool:
    """ Determine if an AST is significant .
    
    Args:
    root: The AST whose significance we want.
    
    Returns:
    True for if it is significant , False otherwise .
    """
    return (
        isinstance(root, Import) or
        isinstance(root, FunctionDef) or
        isinstance(root, If) or
        isinstance(root, ClassDef) or
        isinstance(root, While) or
        isinstance(root, For) or
        isinstance(root, comprehension) or
        isinstance(root, Return)
    )


def get_num_nodes ( root: AST) -> int:
    """ Find the number of nodes for a given tree .

    Args:
    root: The root of the tree whose size we want.

    Returns:
    The number of nodes in the tree .
    """
    return  len(list(ast.walk(root)))



def apply_weights_to_subtrees ( weight: float , subtree : AST) -> float: 
    """ Apply weights to subtrees according to the time por their roots.
    Args:
    weight: The number of nodes in the subtree . subtree : The subtree .

    Returns:
    The weighed weight of the tree .
    """
    new_weight = weight
    if isinstance ( subtree , Import):
      new_weight *= 0.3
    elif isinstance ( subtree , Module ):
      new_weight *= 1
    elif isinstance (subtree , FunctionDef):
      new_weight *= 1.2
    elif isinstance ( subtree , If):
      new_weight *= 0.5
    elif isinstance ( subtree , ClassDef):
      new_weight *= 1
    elif isinstance ( subtree , While ):
      new_weight *= 1
    elif isinstance ( subtree , For):
      new_weight *= 1
    elif isinstance ( subtree , comprehension ):
      new_weight *= 1
    elif  isinstance ( subtree , Return ):
      new_weight *= 1
    return  new_weight


def apply_weights_to_subtrees_mult ( weight: float,  ast_1 : AST, ast_2 : AST) -> float:
    """ Find the average weight of both trees in order to

    Args:
    weight: The weight of the comparison .
    ast_1 : The first compared tree .
    ast_2 : The second compared tree .

    Returns:
    The average of the subtrees ’ weights.
    """
    if weight == 0:
      return  0
    else :
      return  (( apply_weights_to_subtrees ( weight ,  ast_1 )
      + apply_weights_to_subtrees ( weight , ast_2 )) / 2)
	
	
def	compare_many ( programs: list) -> list:
    """ Compare all of the programs in the list.
    
    Args:
    programs: A list of strings with python programs.
    
    Returns:
    A matrix with the similarity rating of between all the programs.
    """
    tree_list = list( map (
    lambda prog: get_significant_subtrees ( ast. parse ( prog)), programs))
    matrix = []
    for  program_1_tree_num  in range (0 , len ( tree_list)):
      for program_2_tree_num in range ( program_1_tree_num , len ( tree_list)): 
        if program_1_tree_num == program_2_tree_num :
          continue
        print( f' comparing { program_1_tree_num } to { program_2_tree_num }')

        subtrees1 = tree_list[ program_1_tree_num ] 
        subtrees2 = tree_list[ program_2_tree_num ]

        result = compare_subtrees(subtrees1, subtrees2, 1000)[0]

        matrix. append (( program_1_tree_num, program_2_tree_num, result)) 
        matrix. append ((program_2_tree_num, program_1_tree_num, result))

      return matrix
    
def main ():
    """ Manual and direct comparison of programs.""" 
    prog1 = "dataset/t2_1.py"
    prog2 = "dataset/t2_2.py"

    with open (prog1 , "r") as source : 
      t1str = source.read ()
      tree1 = ast.parse(t1str, mode = "exec")
    with open (prog2 , "r") as source : 
      t2str = source.read()
      tree2 = ast.parse (t2str, mode = "exec")

    subtree_list1 = get_significant_subtrees ( tree1 ) 
    subtree_list2 = get_significant_subtrees ( tree2 )
    
    similarity = compare_subtrees ( subtree_list1 , subtree_list2 , 10000)[0]

    print(f'The index of similarity between { prog1 } and { prog2 } is: { similarity }')


if __name__ == "__main__": 
  main ()


