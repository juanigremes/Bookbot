def count_words(string):
    words_in_string = string.split()
    return len(words_in_string)

def count_specific_word(text, search):
    res = 0
    words_in_string = text.split()
    for word in words_in_string:
        if search == word:
            res += 1
    return res

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    res = []
    for key,value in dict.items():
        res.append({"char":key, "num":value})
    res.sort(reverse=True, key=sort_on)
    return res

def count_characters(string):
    res = {}
    for char in string:
        char = char.lower()
        if char in res:
            res[char] += 1
        else:
            res[char] = 1
    return res
