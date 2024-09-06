import re
import collections

def count_words(path):
    with open(path, 'r', encoding='utf-8') as textfile:
        all_words = re.findall(r"[0-9a-zA-Z-']+", textfile.read())
        all_words = [word.upper() for word in all_words]
        print(f"\nTotal words : {len(all_words)}")
        
        words_count = collections.Counter(all_words)
        
        print(f"\n Top 2 words")
        for word in words_count.most_common(2):
            print(f"{word[0]}\t{word[1]}")

count_words("myTextFile.txt")