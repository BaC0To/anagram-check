def are_anagrams(string1:str, string2:str)-> bool:
    """Function that checks if two strings are anagrams
    params: two strings
    return: bool
    """
    if (len(string1) == len(string2) and sorted(string1) == sorted(string2)):
        print("The strings are anagrams.")
        return True
    else:
        print("The strings aren't  anagrams.")
        return False
    
#are_anagrams("abc", "cba")