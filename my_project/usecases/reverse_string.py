def main():
    print("reverse the string")
    input = "hello"
    print("reverse",revese(input))

#In this particular example, the slice statement [::-1] means start at the end of the string
# and end at position 0, move with the step -1, negative one, which means one step backwards.
def reverse(str):
    return str[::-1]