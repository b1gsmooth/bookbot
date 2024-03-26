
def main():
    book = "books/frankenstein.txt"
    print(f"--- Begin report of {book} ---")
    with open(book) as f:
        file_contents=f.read()
    count_words(file_contents)
    total_words = count_words(file_contents)
    print(f"The document contains {total_words} words.")
    print("")
    count_letters(file_contents)
    print("--- End report ---")
    
    
def count_words(file_contents):
    words=file_contents.split()
    word_count=len(words)
    return word_count
        
        
    
def count_letters(file_contents):
    char_count = {}  
    lower_words = file_contents.lower()
    for character in lower_words:
        if character.isalpha():
            if character in char_count:
                char_count[character]+= 1
            else:
                char_count[character] = 1
    sorted_characters(char_count)
    return char_count


def sorted_characters(char_count):
    l = []
    for char, count in char_count.items():
        char_dict = {'character': char, 'count': count}
        l.append(char_dict)
    l.sort(reverse=True, key=sort_on)   
    for item in l:
        print(f"The '{item['character']}' character was found {item['count']} times.")
        

def sort_on(dict):
    return dict["count"]
 
    
    
        
if __name__ == '__main__':
    main()