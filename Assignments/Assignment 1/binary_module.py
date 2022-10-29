""" Binary search is trickier than you think.
Remember your binary search should only use one comparison
per while loop, ie, one comparison per halving.
"""

import tools
# uncomment the next line if you want to make some Name objects
from classes import Name

# We recomment using a helper function that does a binary search
# for a Name in a given tested list. This will let you test your
# binary search by itself.




def binary_result_finder(tested, quarantined):
    """ The tested list contains (nhi, Name, result) tuples and
        will be sorted by Name
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the  quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
        Note: You shouldn't sort the tested_list, it is already sorted. Sorting it
        will use lots of extra comparisons!
    """
    total_comparisons = 0
    results = []
    # ---start student section---
    for q_name in quarantined:
        results.append((q_name, None, None))
        total_comparisons += binary_search(tested, q_name, results)
    # ===end student section===
    return results, total_comparisons


def binary_search(tested, q_name, results):
    """ Performs a binary search for q_name in tested.
        If q_name is found, the last entry of results is changed to a tuple of
        information from the entry in results with q_name.
        Returns number of comparisons made.
    """
    comparisons = 0
    lower_bound = 0
    upper_bound = len(tested) - 1
    # Previously lower_bound != upper_bound and upper_bound >= 0
    while lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        comparisons += 1
        if q_name > tested[mid][1]:
            lower_bound = mid + 1
        else:
            upper_bound = mid

    comparisons += 1
    if lower_bound < len(tested) and q_name == tested[lower_bound][1]:
        results[-1] = (q_name, tested[lower_bound][0], tested[lower_bound][2])
        
    return comparisons
    

# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # Tests
    ''' This test adds comparisons
    quarantined = tools.make_name_list(['Bob', 'Abba', 'Faba'])
    tested = tools.make_tested_list(
        ['Bingle', 'Bob', 'Arthur', 'Faba', 'Zabba'], sort_order='name')
    print(quarantined)
    print(tested)
    results, comparisons = binary_result_finder(tested, quarantined)
    print(results, comparisons)
    '''
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Bob'), Name('Abba'), Name('Faba'), Name('Abba')]
    print(binary_result_finder(tested, quarantined))

    tested = []
    quarantined = []
    print(binary_result_finder(tested, quarantined))

    tested = []
    quarantined = [Name('Joe')]
    print(binary_result_finder(tested, quarantined))
    
    tested = [(2, Name('Joe'), True)]
    quarantined = []
    print(binary_result_finder(tested, quarantined))