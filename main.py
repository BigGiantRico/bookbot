def main():
    file_location = "books/frankenstein.txt"
    with open(file_location) as f:
        file_contents = f.read()
    return file_contents, file_location

def count(file_contents):
    counter = 0
    words = file_contents.split()
    for word in words:
        counter += 1
    return counter

def count_chars(file_contents):
    book = file_contents.lower()
    chars = list('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/`~ "\'\\')
    dict = {char:0 for char in book}
    for page in book:
        counter = 0
        for key in dict:
            if page == key:
                counter += 1
        dict[page] += 1
    return dict

def report():
    file_contents, file_location = main()
    word_counter = count(file_contents)
    char_counter = count_chars(file_contents)
    print(f"--- Begin report of {file_location} ---")
    print(f"{word_counter} words found in the document")
    print("")
    for key in char_counter:
        if key != "#" and key != " " and key != ".":
            print(f"The '{key}' character was found {char_counter[key]} times")
    print("--- End Report ---")
report()