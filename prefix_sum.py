# Problems related to Prefix Sum
def pick_from_both_sides(self, A, B):
    """Pick from both sides.

    You have to pick exactly B elements from either left or right end of the array A 
    to get maximum sum
    """
    N = len(A)
    front_sum = sum(A[:B])
    rear_sum = sum(A[-B:])
    if front_sum > rear_sum:
        max_sum = front_sum
    else:
        max_sum = rear_sum
    for i in range(1, B):
        temp = sum(A[0:B-i]) + sum(A[N-i: N])
        if temp > max_sum:
            max_sum = temp
    return max_sum


def prefix_sums(A):
    """Fast calculation of elements in a given slice.

    Consecutive total of the first  0, 1, 2, .. , n elements of the array
    Time Complexity : O(n)
    """
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    """ Find the sum of elements within a given range in O(1) time
        P - Array of Prefix Sums
        x - Start Index
        y - End Index
    """
    return P[y + 1] - P[x]


def mushroom_picker1(A, k, m):
    """Maximum number of mushrooms that can be collected from a given spot
    Brute Force approach 
    Time-Complexity: O(m2)
    For steps -> 0,1,..,m steps, take steps in left_dir and m-p steps in opposite direction
    Input:
        A - Input Array representing the mushrooms available at consecutive spots
        k - Starting position/index in array
        m - No of moves allowed from the starting position
    """
    n = len(A)
    
    max_sum = 0
    for move in range(m):
        left_pos = k - move
        right_pos = left_pos + (m - move)
        if right_pos <= n-1:
            temp_sum = sum(A[left_pos: right_pos+1])
            if temp_sum > max_sum:
                max_sum = temp_sum
    print(max_sum)
    return max_sum

def mushroom_picker2(A, k, m):
    """Maximum number of mushrooms that can be collected from a given spot
    
    Approach - PrefixSum
    TimeComplexity -
    Input:
        A - Input Array representing the mushrooms available at consecutive spots
        k - Starting position/index in array
        m - No of moves allowed from the starting position
    """
    


# Mushroom picker - Brute force testing
A = [2, 3, 7, 5, 1, 3, 9]
initial_position = 4
no_of_steps = 6
mushroom_picker1(A, initial_position, no_of_steps)

A = [1, 2, 3, 4, 5]
result = prefix_sums(A)
print(result)