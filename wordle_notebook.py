#%%
from sample_wordle import sample_list


def solve_worldle(sample_list):
    alphabet=["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letter_dictionary_first={}
    for letter in alphabet:
        letter_dictionary_first[letter]=0

    letter_dictionary_second={}
    for letter in alphabet:
        letter_dictionary_second[letter]=0

    letter_dictionary_third={}
    for letter in alphabet:
        letter_dictionary_third[letter]=0

    letter_dictionary_fourth={}
    for letter in alphabet:
        letter_dictionary_fourth[letter]=0

    letter_dictionary_fifth={}
    for letter in alphabet:
        letter_dictionary_fifth[letter]=0
        

    for word in sample_list:
        for letter in alphabet:
            if letter==word[0]:
                letter_dictionary_first[letter]=letter_dictionary_first[letter]+1
            if letter==word[1]:
                letter_dictionary_second[letter]=letter_dictionary_second[letter]+1
            if letter==word[2]:
                letter_dictionary_third[letter]=letter_dictionary_third[letter]+1
            if letter==word[3]:
                letter_dictionary_fourth[letter]=letter_dictionary_fourth[letter]+1
            if letter==word[4]:
                letter_dictionary_fifth[letter]=letter_dictionary_fifth[letter]+1

    def find_top_5(my_dictionary):
        sorted_dictionary=sorted(my_dictionary.items(), key=lambda x: x[1], reverse=True)
        return sorted_dictionary[0:5]

    best_first=find_top_5(letter_dictionary_first)
    best_second=find_top_5(letter_dictionary_second)
    best_third=find_top_5(letter_dictionary_third)
    best_fourth=find_top_5(letter_dictionary_fourth)
    best_fifth=find_top_5(letter_dictionary_fifth)
    return [best_first, best_second, best_third, best_fourth, best_fifth]


# %%
def refine_list(green_letters, yellow_letters, black_letters, sample_list):
    green_remove_list=[]
    yellow_remove_list=[]
    black_remove_list=[]

    correct_key_list_position=list(green_letters.keys())
    incorrect_key_list_position=list(yellow_letters.keys())
    incorrect_values_list=yellow_letters.values()

    black_letters_list=black_letters.values()


    modified_sample_list=sample_list

    if len(green_letters) !=0:
        for x in range(0,len(sample_list)):
            word=sample_list[x]
            need_to_be_removed=False
            # if the right letter is in the right spot
            for position in correct_key_list_position:
                if word[position] != green_letters[position]:
                    need_to_be_removed=True
                    break
            # if the right letter is in the wrong spot, remove words where the letter is in that spot
            for position in incorrect_key_list_position:
                if word[position]==yellow_letters[position]:
                    need_to_be_removed=True
                    break
            if need_to_be_removed:
                green_remove_list.append(word)

        for word in green_remove_list:
            modified_sample_list.remove(word)

    # taking out words that don't contain the letters 
    for word in sample_list:
        for letter in incorrect_values_list:
            if letter not in word:
                yellow_remove_list.append(word)
    
    for word in yellow_remove_list:
        if word in modified_sample_list:
            modified_sample_list.remove(word)

    #take out words that dont have black letters
    for x in range(0,len(sample_list)):
        word=sample_list[x]
        for letter in word:
            if letter in black_letters_list:
                black_remove_list.append(word)
    
    for word in black_remove_list:
        if word in modified_sample_list:
            modified_sample_list.remove(word)


    
    return modified_sample_list

correct_position_letters_dict={
     4:"s"
}
incorrect_position_letters={
    3:"e"
}
incorrect_letters={
    0:"c",
    1:"o",
    2:"r"

}

refined_list=refine_list(correct_position_letters_dict, incorrect_position_letters, incorrect_letters, sample_list)


# %%
# best_first, best_second, best_third, best_fourth, best_fifth=solve_worldle(refined_list)
best_letters_to_guess=solve_worldle(refined_list)
best_first, best_second, best_third, best_fourth, best_fifth=best_letters_to_guess
print("best first letter", best_first)
print("best second letter", best_second)
print("best third letter",best_third)
print("best fourth letter",best_fourth)
print("best fifth letter",best_fifth)
# %%

def find_best_word(best_letters_to_guess, sample_list):
    print(best_letters_to_guess)    
    
    # what the data looks like
    # [
    # [('c', 410), ('b', 383), ('a', 243), ('s', 193), ('f', 184)],
    #  [('o', 385), ('a', 368), ('r', 274), ('e', 272), ('i', 261)], 
    # [('a', 298), ('i', 257), ('o', 235), ('r', 205), ('e', 191)], 
    # [('e', 509), ('t', 178), ('n', 172), ('l', 171), ('a', 140)], 
    # [('s', 728), ('e', 327), ('y', 220), ('t', 197), ('r', 164)]
    # ]

    # option 1- refine the list down to one word 
    # 1) find the most important letter to guess and its position: s as the 5th letter with 728
    # 2) go through sample list and eliminate all words that don't have the letter in that spot

    # 3) find the next most important: e as the 4th letter with 509. 
    # 4) go through and make sure that there are words left with that letter in that spot
    # 5) if there are no words of that letter in that spot left, find the next best letter: o as 385
    # 6) remove sample list and elimate all words that don't have the letter in that spot
    # 7) repeat steps 3-6 until you have filled in all 5 letters, thus finding the most likely best word to guess
    # note: it won't always be the first letter. The first guess would be S in 5, E in 4, C in 1, O in 2, but R in 3 to make the word CORES

    # 

    # option 2- make the best score
    # 1)
    

    # option 3- try to get the most correct letters in the incorrect spots




find_best_word(best_letters_to_guess, sample_list)


# %%
