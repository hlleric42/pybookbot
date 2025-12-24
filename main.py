from stats import count_word, count_letter, letters_from_greatest
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents        

def main():
    if (len(sys.argv) != 2):
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)
     
     
    path_txt = sys.argv[1].strip()
    
    book_content = get_book_text(path_txt)
    num_words = count_word(book_content)
    count_letter_content = count_letter(book_content)
    sorted_dict_list = letters_from_greatest(count_letter_content)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_txt}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_dict_list:
        print(f"{item['letter']}: {item['count']}")
    sys.exit(0)
main()
