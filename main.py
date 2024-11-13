def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    print(f"--- Beginning of {book_path} ---")
    print(f"There are {word_count} words found in the document\n")
    for letters in letter_count:
        print(f"The {letters["letter"]} character is found {letters["num"]} times in the document")
    print("\n--- End of report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    return len(words)

def sort_on(dict):
    return dict["letter"]

def get_letter_count(alphabet):
    tally = {}
    sorted = []
    for char in alphabet:
        lowered_char = char.lower()
        if lowered_char.isalpha():
            if lowered_char in tally:
                tally[lowered_char] += 1
            else:
                tally[lowered_char] = 1
    for key in tally:
        split_tally = {}
        split_tally["letter"] = key
        split_tally["num"] = tally[key]
        sorted.append(split_tally)
    sorted.sort(reverse=False, key=sort_on)
    return sorted
    
main()