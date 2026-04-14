from stats import count_words, count_characters, sort_dict, count_specific_word  
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_content = file.read()
    return file_content

def format_sorted_dict(sorted_dict):
    res = ""
    for dictionary in sorted_dict:
        if not dictionary['char'].isalpha():
            continue
        res = res + f"{dictionary['char']}: {dictionary['num']}\n"
    return res

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    number_of_words = count_words(book_text)
    character_dict = count_characters(book_text)
    sorted_dict = sort_dict(character_dict)
    formated_sorted_dict = format_sorted_dict(sorted_dict)

    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {file_path}...\n"
        f"----------- Word Count ----------\n"
        f"Found {number_of_words} total words\n"
        f"--------- Character Count -------\n"
        f"{formated_sorted_dict}\n"
    )

    first_run = True
    while True:
        
        print("--------------------")

        if first_run:
            answer = input("\nQuerés buscar una palabra? --> si / no  + Enter\n")
        else:
            answer = input("\nQuerés buscar otra palabra? --> si / no  + Enter\n")
        
        if answer == "si":
            first_run = False
            word = input("Qué palabra?\n")
            res = count_specific_word(book_text, word)
            print(f"\nLa palabra {word} aparece {res} veces en el texto\n")
        elif answer == "no":
            print("=============== END ===============")
            return
        else:
            print("La respuesta es si o no\n")



main()
