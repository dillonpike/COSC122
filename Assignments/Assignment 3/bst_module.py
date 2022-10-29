"""Module for finding test results of quarantined people using a BST."""
import sys
from classes3 import Name, BstNode, bst_nested_repr
sys.setrecursionlimit(10**6)

# note you might want to import other things here for testing
# but your submission should only include the import line above.
import tools # remove when submitting


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
    node = BstNode(key, value)
    current = root
    inserted = False
    while inserted is False:
        comparisons += 1
        if key < current.key:
            if current.left is None:
                current.left = node
                inserted = True
            else:
                current = current.left
        elif key > current.key:
            comparisons += 1
            if current.right is None:
                current.right = node
                inserted = True
            else:
                current = current.right
        else:
            comparisons += 1
            current.value = value
            inserted = True
    # ===end student section===
    return comparisons



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
    current = root
    found = False
    while found is False:
        comparisons += 1
        if key < current.key:
            if current.left is None:
                found = True
            else:
                current = current.left
        elif key > current.key:
            comparisons += 1
            if current.right is None:
                found = True
            else:
                current = current.right
        else:
            comparisons += 1
            value = current.value
            found = True
    # ===end student section===
    return value, comparisons



def min_key_in_bst(root):
    """ Returns the minimum key value in the bst starting at root.
    Returns None if root is None
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    if root is not None:
        current = root
        while current.left is not None:
            current = current.left
        result = current.key
    # ===end student section===
    return result




def max_key_in_bst(root):
    """ Returns the maximum key value in the bst starting at root.
    Returns None if root is None.
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    if root is not None:
        current = root
        while current.right is not None:
            current = current.right
        result = current.key
    # ===end student section===
    return result




def num_nodes_in_tree(root):
    """ Returns the number of nodes in the tree starting at root.
    If the root is None then the number of nodes is zero.
    """
    num_nodes = 0
    # ---start student section---
    if root is not None:
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
    if root is not None and (root.left is not None or root.right is not None):
        depth = 1 + max(bst_depth(root.left), bst_depth(root.right))
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
    '''
    if root is not None:
        result_list = bst_in_order(root.left) + [(root, root.value)] + bst_in_order(root.right)
    '''
    if root is not None:
        bst_in_order(root.left, result_list)
        result_list.append((root.key, root.value))
        bst_in_order(root.right, result_list)
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
    bst = None
    if len(tested) > 0:
        nhi, name, result = tested[0]
        bst = BstNode(name, (nhi, result))
        for i in range(1, len(tested)):
            nhi, name, result = tested[i]
            comparisons += bst_store_pair(bst, name, (nhi, result))
            
    for name in quarantined:
        results.append((name, None, None))
        if len(tested) > 0:
            value, comps = get_value_from_tree(bst, name)
            comparisons += comps
            if value is not None:
                nhi, result = value
                results[-1] = (name, nhi, result)
    # ===end student section===

    return results, comparisons


if __name__ == '__main__':
    # put your own simple tests here
    # you don't need to submit this code
    print("Add some tests here...")

    tested = []
    quarantined = []
    print(bst_result_finder(tested, quarantined))

    tested = []
    quarantined = [Name('Joe')]
    print(bst_result_finder(tested, quarantined))
    
    tested = [(2, Name('Joe'), True)]
    quarantined = []
    print(bst_result_finder(tested, quarantined))
    
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Bob'), Name('Abba'), Name('Faba'), Name('Abba')]
    print(bst_result_finder(tested, quarantined))
    
    quarantined = tools.make_name_list(['Bob', 'Abba', 'Faba'])
    tested = tools.make_tested_list(['Bob', 'Abba', 'Faba', 'Joe'])
    print(bst_result_finder(tested, quarantined))
