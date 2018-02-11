

def pretty_print_dict(dictionary: dict) -> None:
    print("{")
    for item in dictionary:
        print(item, ":", dictionary[item])

    print("}")