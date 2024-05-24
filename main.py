def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    counter = get_letter(text)
    print(f"{counter} letters found in the document")
    print_report(book_path, num_words, counter)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter(text):
        # Convert the text to lowercase
    text = text.lower()
    
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the string
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def print_report(book_path, num_words, counter):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    sorted_char_count = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_char_count:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

main()

