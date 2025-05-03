# obtain a list of files in the input directory
import os

from homework.src._internals import read_all_lines, preprocess_lines, split_in_words, count_words, write_count_words

def main():

     ## mover a la funcion "read_all_lines"
    all_lines = read_all_lines()
    
     ## mover a "preprocess_lines"
    all_lines = preprocess_lines(all_lines)

    ## mover "split_in_words"
    words = split_in_words(all_lines)

    ## mover a "count_words"
    counter = count_words(words)

    # count the frequency of the words in the files in the input directory
    # counter={}
    # for filename in input_file_list:
    #     with open('data/input/'+filename) as f:
    #         for l in f:
    #             for w in l.split( ):
    #                 w = w.lower().strip(",.!?")
    #                 counter[w] = counter.get(w, 0) + 1

    ##
    write_count_words(counter)

if __name__ == "__main__":
    main()