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


def chars_print(items: list[tuple[str, int]]) -> None:
    for item in items:
        key, value = item
        clean_key = key.replace("\ufeff", "<BOM>")  # make BOM character readable
        print(f"{clean_key}: {value}")
