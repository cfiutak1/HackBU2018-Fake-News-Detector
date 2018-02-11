import csv


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

def print_csv(csv_file:str) -> None:
    reader = csv.reader(open(csv_file, "r"))
    accum = 0
    for row in reader:
        print(accum, row)
        accum += 1

print_csv("fakenews_training.csv")