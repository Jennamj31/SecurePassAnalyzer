import itertools
import re

def leetspeak_variants(word):
    leet_map = {'a': '4', 'e': '3', 'l': '1', 'o': '0', 's': '5'}
    variants = [word]
    for i in range(len(word)):
        if word[i].lower() in leet_map:
            for var in list(variants):
                variants.append(var[:i] + leet_map[word[i].lower()] + var[i+1:])
    return set(variants)

def generate_wordlist(inputs, years=(2000, 2025)):
    base_words = set()
    for word in inputs:
        base_words.update(leetspeak_variants(word))
    
    combos = set()
    for word in base_words:
        combos.add(word)
        for year in range(*years):
            combos.add(f"{word}{year}")
            combos.add(f"{year}{word}")
    
    return sorted(combos)
