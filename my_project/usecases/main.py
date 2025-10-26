from usecases.anagram import anagram
from usecases.reverse_string import reverse
from usecases.longest_subsequence import max_seq
from usecases.quicksort import sort

def main_function():
    print("Hello, this is the main function.")
    print()

    print("Anagram")
    print(anagram("Tar", "Rat"))
    print(anagram("Arc", "Orc"))
    print()

    print("Reverse string")
    print(reverse("reverse"))
    print()

    print("Longest sustring")
    input = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
    #input = [1, 9, 3, 10, 4, 20, 2]
    res = max_seq(input)
    print("max seq:", res)
    print()

    print("Quick sort")
    input = [10,3,11,13,2,5,20,8,45]
    sort(input)
    for i in input:
        print(i)


if __name__ == "__main__":
    main_function()
