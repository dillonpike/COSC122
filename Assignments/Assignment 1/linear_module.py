""" Linear/sequential searching """
import tools
# uncomment the next line if you want to make some Name objects
from classes import Name


def linear_result_finder(tested_list, quarantined):
    """ The tested list contains (nhi, Name, result) tuples
        and isn't guaranteed to be in any order
        quarantined is a list of Name objects
        and isn't guaranteed to be in any order
        This function should return a list of (Name, nhi, result)
        tuples and the number of comparisons made
        The result list must be in the same order
        as the quarantined list.
        The nhi and result should both be set to None if
        the Name isn't found in tested_list
        You must keep track of all the comparisons
        made between Name objects.
        Your function must not alter the tested_list or
        the quarantined list in any way.
    """
    comparisons = 0
    results = []
    # ---start student section---
    for q_name in quarantined:
        results.append((q_name, None, None))
        for nhi, t_name, result in tested_list:
            comparisons += 1
            if q_name == t_name:
                results[-1] = (q_name, nhi, result)
                break
    # ===end student section===
    return results, comparisons


# Don't submit your code below or pylint will get annoyed :)
if __name__ == '__main__':
    # Tests
    tested = []
    quarantined = []
    print(linear_result_finder(tested, quarantined))    
    
    tested = [(1, Name('Lee'), True)]
    quarantined = []
    print(linear_result_finder(tested, quarantined))
    
    tested = []
    quarantined = [Name('Bob')]
    print(linear_result_finder(tested, quarantined))    
    
    tested = [(1, Name('Lee'), True)]
    quarantined = [Name('Bob')]
    print(linear_result_finder(tested, quarantined))
    
    tested = [(1, Name('Lee'), True)]
    quarantined = [Name('Lee')]
    print(linear_result_finder(tested, quarantined))    

    filename = "test_data/test_data-2i-2r-1-a.txt"
    tested, quarantined, expected_results = tools.read_test_data(filename)
    print(linear_result_finder(tested, quarantined))
    
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Bob'), Name('Abba'), Name('Faba'), Name('Abba')]
    print(linear_result_finder(tested, quarantined))
    
    # Worst case test
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Joe'), Name('Mama'), Name('Daniel'), Name('Pallesen')]
    results, comparisons = linear_result_finder(tested, quarantined)
    print(results)
    print("Expected comparisons:", len(tested) * len(quarantined)) # O(mn)
    print("Actual comparisons:", comparisons)
    
    # Best case, m < n
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Arthur'), Name('Bingle'), Name('Faba'), Name('Bob')]
    results, comparisons = linear_result_finder(tested, quarantined)
    print(results)
    print("Expected comparisons:", len(quarantined)*(len(quarantined)+1)/2) # O(m^2)
    print("Actual comparisons:", comparisons)
    
    # n items in both, and every name in quarantined is in tested
    tested = [(3, Name('Arthur'), True), (1, Name('Bingle'), True), 
              (2, Name('Bob'), True), (4, Name('Faba'), True), 
              (5, Name('Zabba'), True)]
    quarantined = [Name('Arthur'), Name('Bingle'), Name('Bob'), Name('Faba'), 
                   Name('Zabba')]
    results, comparisons = linear_result_finder(tested, quarantined)
    print(results)
    length = len(quarantined) 
    print("Expected comparisons:", length*(length + 1)/2) # n(n+1)/2
    print("Actual comparisons:", comparisons)    
    