import time

if __name__ == "__main__":

    time_start = time.time()

    # Creating the list
    word_list = []
    time_table = time.time() - time_start
    print(f"Time spent making the table: {time_table}s")


    # Storing the English words to the list
    english_words_list = open('words_alpha.txt', 'r')
    english_words = english_words_list.readlines()
    english_words_list.close()

    for word in english_words:
        word_list.append(word.rstrip('\n'))

    time_insert = time.time() - time_table - time_start
    print(f"Time spent inserting: {time_insert:.4f}s")


    # Finding the common words from the list of Finnish words
    finnish_words_list = open('kaikkisanat.txt', 'r', encoding="utf-8")
    finnish_words = finnish_words_list.readlines()
    finnish_words_list.close()

    common_words = 0
    for word in finnish_words:
        if word.rstrip('\n') in word_list:
                common_words += 1

    time_search = time.time() - time_insert - time_table - time_start
    print(f"Time spent searching: {time_search:.4f}s")


    # Printing the answer
    print(f"\nCOMMON WORDS: {common_words}")
