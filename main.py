from stats import *

import sys
    
def main():
    try:
        path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(path)
    # print(content)
    num_words = count_words(content)
    # print(f"{num_words} words found in the document")
    
    dict_unique_letters_count = count_unique_letters(content)
    # print(dict_unique_letters_count)
    
    sorted_list_unique_letters_count = sorted_unique_letters(dict_unique_letters_count)
    # print(sorted_list_unique_letters_count)
    
    unique_alpha_str = ""
    for i in sorted_list_unique_letters_count:
        if i["char"].isalpha():
            unique_alpha_str += f"{i["char"]}: {i["num"]}\n"
    
    # print(unique_alpha_str)
    
    
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{unique_alpha_str}
============= END ===============
          """)
    
    
    
    
    
main()