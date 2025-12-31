def row_print(text="", sign="=", width=34) -> None:
    """Prints a row of signs and text"""
    x = (width - len(text) - 2) / 2
    if x.is_integer():
        x = int(x)
        y = x
    else:
        x = int(x)
        y = x + 1
    print(f"{sign * x} {text} {sign * y}")


def chars_print(items={}) -> None:
    for item in items:
        char = item['char']
        num = item['num']
        if char.isalpha():
            print(f"{char}: {num}")
