def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(word_count("hello world how are you how can I help you"))