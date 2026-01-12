from collections import Counter

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", ""). lower()
    str2 = str2.replace(" ", ""). lower()
    return Counter(str1) == Counter(str2) 

    