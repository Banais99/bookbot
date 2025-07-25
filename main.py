from stats import get_num_words,char_count,new_list
def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents


def main():
    text = get_book_text("books/frankenstein.txt")
    count= get_num_words(text)
    char_counts=char_count(text)
    lista= new_list(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in lista:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()