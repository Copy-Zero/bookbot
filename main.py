def get_words(string):
    word_count = string.split()
    return len(word_count)


def char_count(string):
    char_count = {}
    for raw_char in string:
        char = raw_char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def scrub_letter(ltr_dict):
    letters_only = []
    for letter, qty in ltr_dict.items():
        if letter.isalpha():
            ltr_list = [letter, qty]
            letters_only.append(ltr_list)

    return letters_only


def final_report(book_title, total_words, letter_counts):
    print(f"--- Book Report for {book_title} ---")
    print(f"{total_words} words were found in the document")
    for group in letter_counts:
        print(f"The {group[0]} character was found {group[1]} times")

    print("--- End Report ---")


book_file = "books/frankenstein.txt"
with open(book_file) as f:
    file_contents = f.read()

letter_counts = char_count(file_contents)

final_counts = scrub_letter(letter_counts)
final_counts.sort()


total_words = get_words(file_contents)
final_report(book_file, total_words, final_counts)
