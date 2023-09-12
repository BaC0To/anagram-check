class Anagram:
    """Class Anagram
    """
    
    @staticmethod      
    def strings_anagram_checker(input_string1:str, input_string2:str):
        """function that checks if input parameters are strings and whether they are anagrams by three conditions
        parameters: input_string1, input_string2
        return: bool isAnagram final result
        """
        list_of_chars_string1 = []
        list_of_chars_string2 = []
        isAnagram = False

        try:

            if len(input_string1) == len(input_string2): # if parameters are string check their equal length (1st rule for anagram)
        
                for item1 in input_string1:
                    list_of_chars_string1.append(item1)

                for item2 in input_string2:
                    list_of_chars_string2.append(item2)

                    
                presence_counter = 0
                for ch in list_of_chars_string1: 
                    if ch in list_of_chars_string2: # 2nd rule if all ch from 1st list present in 2nd list
                        presence_counter += 1
                

                if ((presence_counter == len(input_string1)) and (presence_counter == len(input_string2))): #3rd rule if presence counter equals both sizes of 2 list
                    isAnagram = True

            else:
                print("Strings lengths are different --> so definitely are no anagrams!")
                isAnagram = False

            return isAnagram
        
        except (TypeError) as exc:
                print(f"Oops!  That {exc}.Try again with strings...")


