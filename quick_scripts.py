

def pretty_print_dict(dictionary: dict) -> None:
    """
    Formatted printing for a given dictionary

    @param dictionary, a dictionary to be printed
    @return None
    """
    print("{")
    for item in dictionary:
        print(item, ":", dictionary[item])

    print("}")
