def word_count(text):
    word_list = text.split()
    return len(word_list)

def char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_dict(dict):
    def sort_on(items):
        return items["num"]
    result = []
    for char, num in dict.items():
        result.append({"char":char, "num":num})
    result.sort(reverse=True, key=sort_on)
    return result