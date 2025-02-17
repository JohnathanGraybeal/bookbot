def main():
    text = read_book("books/frankenstein.txt")
    char_count = count_characters(text)
    char_count.sort(key=sort_on, reverse=True)
    print(char_count)
    
def read_book(path_to_book):
    with open(path_to_book) as f:
        return f.read()

def count_characters(text):
    word_count = {}
    for character in text:
        if character.lower() in word_count and character.isalpha():
            word_count[character.lower()] = word_count[character.lower()] + 1
        elif character.lower() not in word_count and character.isalpha():
            word_count[character.lower()] = 1
    return [{key: value} for key, value in word_count.items()]

def sort_on(dict):
    return list(dict.values())[0]

    
main()
