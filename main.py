#!/usr/bin/python3


def count_each_letter(text: str):
    count = {}

    for c in text:
        if not c.isalpha():
            continue
        lowercase = c.lower()
        if lowercase not in count:
            count[lowercase] = 1
        else:
            count[lowercase] += 1
    return count


def count_words(text: str):
    count = 0
    for _ in text.split():
        count += 1
    return count


def read_text(file_path):
    with open(file_path) as book:
        return book.read()


def main():
    book = "books/frankenstein.txt"
    content = read_text(book)
    words = count_words(content)
    letters = count_each_letter(content)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    sorted_letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
    for letter, count in sorted_letters:
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")


main()
