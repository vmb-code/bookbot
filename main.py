path_to_file = "./books/frankenstein.txt"


def sort_on(dict):
    return dict["num"]


with open(path_to_file) as f:
    char_count = {}
    file_contents = f.read()
    for char in file_contents:
        char = char.lower()  # Convert to lowercase
        if char in char_count:
            char_count[char]["num"] += 1
        else:
            char_count[char] = {"name": char, "num": 1}

    # Sort the dictionary values by "num" in descending order
    sorted_char_list = sorted(char_count.values(), key=lambda d: d["num"], reverse=True)
    for counted in sorted_char_list:
        print(f"The {counted['name']} was found {counted['num']}")
