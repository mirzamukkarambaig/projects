def identify_duplicates(string: str) -> dict:
    """Identify duplicate characters in a string."""
    duplicates = {}
    for char in string:
        if char in duplicates:
            duplicates[char] += 1
        else:
            duplicates[char] = 1
    return duplicates

string = "Hello World!"
print(identify_duplicates(string))