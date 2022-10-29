"""Module for finding test results of quarantined people using a BST."""
import sys
from classes3 import Name, BstNode, bst_nested_repr
sys.setrecursionlimit(10**6)

# note you might want to import other things here for testing
# but your submission should only include the import line above.
import tools


def bst_store_pair(root, key, value):
    """
    Stores the key, value pair in the BST tree that stars at the given root.
    This function updates an existing tree so:
      - the root must be an existing BstNode.
      - if root is None an exception is raised.
    Returns the number of key comparisons used.
    Assumes the key is unlikely to already be in the tree and shouldn't check
    for the key being in the current node first, in a similar fashion to the
    binary search from assignment 1. You must figure out which key comparison
    is done first. The simple BST tests will help you figure it out.
    If the key already exists then the value in that node should be updated
    to the given value. This means that keys in the bst will be unique.
    NOTE: You shouldn't use recursion here as it will eventually cause
    Python to blow-up when testing large, worst case, data sets.
    """
    comparisons = 0
    if root is None:
        raise ValueError("I need to have something to add to!")
    # ---start student section--- 
    node = root
    while True:
        comparisons += 1
        if key < node.key:
            # Insert to the left
            if node.left is None:
                node.left = BstNode(key, value)
                return comparisons
            else:
                node = node.left
                
        elif key > node.key:
            comparisons += 1
            # Insert to the right
            if node.right is None:
                node.right = BstNode(key, value)
                return comparisons
            else:
                node = node.right
        else:
            comparisons += 1
            node.value = value
            return comparisons
            
    return comparisons        
    # ===end student section===

def get_value_from_tree(root, key):
    """ Returns the value associated with the given key,
    or None if the key is not present in the tree.
    Your search should only check that the root contains the key
    after ruling out that the key can't be in a sub tree.
    That is check if you need to search one of the sub trees first.
    The tests expect a specific comparison to be first, you will
    need to figure out which one it is :)
    Returns the value/None and the number of key comparisons used.
    NOTE: You shouldn't use recursion here as it will eventually cause
    Python to blow-up when testing large, worst case, data sets.
    """
    comparisons = 0
    value = None
    # ---start student section---

    node = root
    while True:
        comparisons += 1
        if key < node.key:
            # Check to the left
            if node.left is None:
                break
            else:
                node = node.left
                
        elif key > node.key:
            comparisons += 1
            # Check to the right
            if node.right is None:
                break
            else:
                node = node.right
        else:
            comparisons += 1
            value = node.value
            break
            
            
            
    # ===end student section===
    return value, comparisons



def min_key_in_bst(root):
    """ Returns the minimum key value in the bst starting at root.
    Returns None if root is None
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    if root is None:
        pass    
    else:
        node = root
        while result is None:	
            if node.left is None:
                result = node.key
            else:
                node = node.left
    # ===end student section===
    return result




def max_key_in_bst(root):
    """ Returns the maximum key value in the bst starting at root.
    Returns None if root is None.
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    if root is None:
        pass    
    else:
        node = root
        while result is None:	
            if node.right is None:
                result = node.key
            else:
                node = node.right
    # ===end student section===
    return result




def num_nodes_in_tree(root):
    """ Returns the number of nodes in the tree starting at root.
    If the root is None then the number of nodes is zero.
    """
    num_nodes = 0
    # ---start student section---
    if root is None:
        pass
    elif root.left is None and root.right is None:
        num_nodes += 1
    else:
        num_nodes += num_nodes_in_tree(root.left)
        num_nodes += num_nodes_in_tree(root.right)
        num_nodes += 1
    # ===end student section===
    return num_nodes


def bst_depth(root):
    """ The level of a node is the number of edges from the root to the node
        The depth is the maximum level of nodes in a tree.
        Remember, the level of a node is how many edges there are on a path
        from the root to the node.
        So, the depth of a tree starting at the root is:
        - zero if the root is None
        - zero if the root has no children
        - 1 + the max depth of the trees starting at the left and right child
    """
    depth = 0
    # ---start student section---
    if root is None or (root.left is None and root.right is None):
        pass
    
    else:
        depth_left, depth_right = bst_depth(root.left), bst_depth(root.right)
        if depth_left > depth_right:
            depth = depth_left + 1
        else:
            depth = depth_right + 1
    # ===end student section===
    return depth


def bst_in_order(root, result_list=None):
    """ Returns a list containing (key, value) tuples
    from the bst, in the order of the keys.
    Basically does an in order traversal of the tree
    collecting (key, value) pairs as each node is visited.
    Returns an empty list if the root is None.
    This function shouldn't use any key comparisons!
    """
    if result_list is None:
        result_list = []
    # ---start student section---
    if root is not None:       
        result_list = bst_in_order(root.left, result_list=result_list)
        result_list.append((root.key, root.value))
        result_list = bst_in_order(root.right, result_list=result_list)
    # ===end student section===
    return result_list


def bst_result_finder(tested, quarantined):
    """This function takes two lists as input.
    tested contains (nhi, Name, result) tuples for people that have been tested
    quarantined contains the names of people in quarantine

    You cannot assume the lists are in any particular order, ie, you cannot
    assume that either list will be sorted.

    You can assume that there are no duplicate values in either list,
    ie, within each list any name only appears once.

    The function returns a list and an integer, ie, results, comparisons.
    The results list contains (name, nhi, result) tuples for each
    name in the quarantined list. If the name isn't in the tested list
    then the nhi and result should be set to None.
    The integer is the number of Name comparisons the function made.

    You must use a BST to store the tested data and
    use the get_value_from_tree function for looking up names
    in the tree. Using name for the key and a (nhi, result) tuple
    for the value makes sense.

    """
    comparisons = 0
    results = []
    # ---start student section---
    if len(quarantined) < 1:
        pass
    elif len(tested) < 1:
        for name in quarantined:           
            results.append((name, None, None))             
    else:
        root = None
        for person in tested:
            key = person[1]
            value = (person[0], person[2])
            if root is None:
                root = BstNode(key, value)
            else:
                comps = bst_store_pair(root, key, value)
                comparisons += comps
        for name in quarantined:
            result, comps = get_value_from_tree(root, name)
            comparisons += comps
            if not result is None:
                results.append((name, result[0], result[1]))
            else:
                results.append((name, None, None))        
            
    # ===end student section===
    return results, comparisons




def smart_bst_result_finder_v1(tested, quarantined):
    """
    Note: this function is an optional bonus exercise
    and isn't worth any marks.
    
    This function has similar input/output as the
    original bst_result_finder but it utilises a much
    faster way of building the bst when the tested
    list is fully sorted by name. If the tested list
    is fully sorted by name then you should write
    an alternative method for adding all the records
    to the bst.
    
    If the tested list isn't fully sorted by name then
    the old/slow method is still used.
    You should leave the get_value_from_tree function
    the same, and use it as before...
    """
    comparisons = 0
    results = []
    # ---start student section---
    pass
    # ===end student section===
    return results, comparisons


def smart_bst_result_finder_v2(tested, quarantined):
    """ 
    Note: this function is a bonus extra questions and
    isn't worth any marks.
    
    This function has similar input/output as the
    original bst_result_finder but it utilises a much
    faster way of building the bst when the tested
    list is fully sorted by name.

    If the tested list was sorted and the quarantined list
    is also sorted then we can speed up the getting values
    from the tree in a way similar to the dual method from
    assignment 2. Doing this means you won't use the 
    normal get_value_from_tree function.

    If the tested list isn't fully sorted by name then
    the old method is still used for building the bst
    and for looking up quarantined names in the tree.

    """
    comparisons = 0
    results = []
    # ---start student section---
    pass
    # ===end student section===
    return results, comparisons


if __name__ == '__main__':
    # put your own simple tests here
    # you don't need to submit this code
    print("Add some tests here...")



#root = BstNode(2, "a")
#print(bst_store_pair(root, 3, 'b'))
#print(bst_store_pair(root, 1, 'c'))
#print(bst_store_pair(root, 5, 'd'))
#print(bst_store_pair(root, 3, 'e'))
#print(bst_nested_repr(root))
#print(bst_in_order(root))

quarantined = tools.make_name_list(['Bob', 'Abba', 'Faba', 'Papa']) # 
#quarantined = tools.make_name_list(['a','b','c','d'], sort_order='name')
tested = tools.make_tested_list(
    ['Bingle', 'Bob', 'Arthur', 'Faba', 'Zabba'], sort_order='name')    
#tested = tools.make_tested_list(
    #['a','c'], sort_order='name')     
print(quarantined)
print(tested)
results, comparisons = bst_result_finder(tested, quarantined)
print(results, comparisons)