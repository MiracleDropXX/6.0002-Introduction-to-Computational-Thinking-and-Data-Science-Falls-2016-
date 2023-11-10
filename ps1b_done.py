###########################
# 6.0002 Problem Set 1b: Space Change
# Name: An Nguyen
# Collaborators:
# Time: 2023-11-09
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    
    if (target_weight, egg_weights) in memo:
        result = memo[(target_weight, egg_weights)]
    elif target_weight == 0 :
        result = 0
    else:
        eligible_eggs = tuple(weight for weight in egg_weights if weight <= target_weight)  # Tuple of eligible weights
        exploratory_result = []
        for egg_totake in eligible_eggs:
            tmp_result = 1+ dp_make_weight(eligible_eggs, target_weight-egg_totake , memo)
            exploratory_result.append(tmp_result)
        result = min(exploratory_result)
    # update memo
    memo[(target_weight, egg_weights)] = result
    
    return result
    pass




# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 2, 3, 4, 7, 33)
    n = 75
    print(f"Egg weights = {egg_weights}")
    print(f"n = {n} \n")
    
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    
    
