# coding: utf-8

import csv
import json
import string
import pickle

def main(filename):
    texfile=open(filename)
    lines=txtfile.readlines()
    all_words=[]
    for line in lines:
        word=line.split()
        for word in words:
            word=word.strip(string.punctuation)
            if word!=(''):
                all_words.append(word)
    from collections import Counter
    counter=Counter(all_words)
    
    with open('wordcount.csv', 'w', newline='')as fin:
        writer = csv.writer(fin, delimister=',')
        writer.writerow(['word','count'])
        for idx, val in counter.most_common():
            writer.writerow([idx, val])
            
    with open('wordcount.json','w')as json_file:
        json.dump(counter,json_file)
    
    with open('wordcount.pkl','wb')as pkl_file:
        pickle.dump(counter,pkl_file)
        
if __name__ == '__main__':
    main("i_have_a_dream.txt")


    ...

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly


if __name__ == '__main__':
    main("i_have_a_dream.txt")
