def strings_anagram_checker(*parameters:str):
    """function that checks if input parameters are strings and whether they are anagrams
    
    parameters: any
    return: bool isAnagram result"""

    list_of_chars_string1 = []
    list_of_chars_string2 = []
    isAnagram = False

    try:

        if len(input_string1) == len(input_string2): # if parameters are string check their equal length (1st rule for anagram)
    
            for item in input_string1:
                list_of_chars_string1.append(item)

            for item in input_string2:
                list_of_chars_string2.append(item)

                  
            counter = 0
            for ch in list_of_chars_string1:
                 if ch in list_of_chars_string2:
                      counter += 1
            

            if ((counter == len(input_string1)) and (counter == len(input_string2))):
                print("The strings are anagrams...")
                isAnagram = True
            else:
                print("The strings are not anagrams...")

        else:
            print("Strings lengths are different --> so definitely are no anagrams!")

        return isAnagram
    
    except (TypeError) as exc:
            print(f"Oops!  That {exc}.Try again with strings...")

#dusty = study
#cat = act
#state = taste

input_string1 = "cat"
input_string2 = "act"

actual_result = strings_anagram_checker(input_string1, input_string2)
print(actual_result)