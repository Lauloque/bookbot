def count_words(text="") -> int:
    return len(text.split())

def count_chars(text="") -> dict:
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', ',', '!', '?', ':', ';', '(', ')', '"', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chars_list = []

    for char in chars:
        count = 0
        for letter in text:
            if letter.lower() == char:
                count += 1
        chars_list.append({
            "char": char,
            "num": count
        })

    return chars_list

def sort_on_nums(items):
    return items["num"]
