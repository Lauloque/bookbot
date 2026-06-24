def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(item: tuple[str, int]) -> int:
    return item[1]


def chars_dict_to_sorted_list(count: dict[str, int]) -> list[tuple[str, int]]:
    chars = []
    for key in count.keys():
        _ = key, count[key]
        chars.append(_)
    return sorted(chars, key=sort_on, reverse=True)


def count_words(text="") -> int:
    return len(text.split())
