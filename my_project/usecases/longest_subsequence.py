
# Given an array of numbers, find the longest consecutive subsequence.
# Input: arr[] = {36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42}
# Explanation:
# output subsequence 36, 35, 34, 33, 32 is the longest
# Seq count Output: 5
# subsequence of consecutive elements.
# Ex: Input arr[] = {1, 9, 3, 10, 4, 20, 2}
# output subsequence 1, 2, 3, 4 is the longest
# Seq count Output: 4

def max_seq(input):
    sortedinput = sorted(input)
    if len(input) == 0: return 0
    count = 1
    max = 1
    index = 0
    for i in sortedinput[1:]:
        index += 1
        if (i == sortedinput[index-1]+1):
            count += 1
        else:
            count = 1

        if count > max:
            max = count

    return max