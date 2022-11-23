import time

if __name__ == "__main__":

    time_start = time.time()

    time_table = time.time() - time_start
    print(f"Time spent making the table: {time_table}")

    eng_words = open('words_alpha.txt', 'r')
    word_list = []
    while True:
        line = eng_words.readline()
        if len(line) < 1:
            break
        else:
            word_list.append(line.rstrip('\n'))
            
    eng_words.close()

    time_insert = time.time() - time_table - time_start
    print(f"Time spent inserting: {time_insert}")
    common = 0

    
    fin_words = open('kaikkisanat.txt', 'r', encoding="utf-8")
    while True:
        line = fin_words.readline()
        if len(line) < 1:
            break
        else:
            if line.rstrip('\n') in word_list:
                common += 1
    fin_words.close()

    time_search = time.time() - time_insert - time_table - time_start
    print(f"Time spent searching: {time_search}")

    print(f"Common words: {common}")
