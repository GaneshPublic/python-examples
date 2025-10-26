
# Check whether 2 strings are anagrams of each other
# Definition: An anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase, typically
# using all the original letters exactly once.
# Ex: Tar = Rat
# Arc = Car
# Elbow = Below
# State = Taste
# Logic
# a = sort(word1.split())
# b = sort(word2.split())
# if a = b "anagram"
# else "not an anagram"
#

def anagram(w1, w2):
    a = sorted(w1.lower())
    b = sorted(w2.lower())

    if a == b :
        return True
    else:
        return False





