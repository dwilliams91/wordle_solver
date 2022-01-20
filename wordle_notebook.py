#%%
from sample_wordle import sample_list
# import random from numpy

# this returns a 5X5 list of the 5 most common letter in each spot
def best_5_letters_in_each_spot(sample_list):
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
# this refines the list depending on the guess. 
def refine_list(green_letters=None, yellow_letters=None, black_letters=None, sample_list=None):
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

# sample data
# correct_position_letters_dict={
#      4:"s"
# }
# incorrect_position_letters={
#     3:"e"
# }
# incorrect_letters={
#     0:"c",
#     1:"o",
#     2:"r"


# this looks through the top 5X5 list, and finds the best letter
def find_best_letter_to_guess(best_letters_to_guess, already_guessed_letter):
    current_best_number=0
    current_best_letter_position=0
    current_best_letter=""

    for x in range(0,len(best_letters_to_guess)):
        for i in range(0,4):
            item=best_letters_to_guess[x]
            best_positional_letter=item[i]   
            # print(best_positional_letter," is compared to ('", current_best_letter, "', ", current_best_number)

            if best_positional_letter[1]>current_best_number and best_positional_letter[0] not in already_guessed_letter:
                current_best_number=best_positional_letter[1]
                current_best_letter_position=x
                current_best_letter=best_positional_letter[0]


   
    return {
        current_best_letter_position:current_best_letter
    }




# %%
def make_guess(list_of_words):
    # initial list
    list_of_letters_guessed=[]
    best_5_letters_to_guess=best_5_letters_in_each_spot(list_of_words)
    print("FIRST", best_5_letters_to_guess)

    best_letter_1=find_best_letter_to_guess(best_5_letters_to_guess,[])
    item_to_append=list(best_letter_1.values())
    list_of_letters_guessed.append(item_to_append[0])
    list_after_first_letter=refine_list(best_letter_1,{}, {}, list_of_words)

    # second letter
    best_5_letters_to_guess=best_5_letters_in_each_spot(list_after_first_letter)
    print("SECOND", best_5_letters_to_guess)

    best_letter_2=find_best_letter_to_guess(best_5_letters_to_guess, list_of_letters_guessed)
    item_to_append=list(best_letter_2.values())
    list_of_letters_guessed.append(item_to_append[0])
    list_after_second_letter=refine_list(best_letter_2,{}, {}, list_after_first_letter)
    
    # third letter
    best_5_letters_to_guess=best_5_letters_in_each_spot(list_after_second_letter)
    print("THIRD", best_5_letters_to_guess)
    best_letter_3=find_best_letter_to_guess(best_5_letters_to_guess,list_of_letters_guessed)
    item_to_append=list(best_letter_3.values())
    list_of_letters_guessed.append(item_to_append[0])
    list_after_third_letter=refine_list(best_letter_3,{}, {}, list_after_second_letter)

    # forth letter
    best_5_letters_to_guess=best_5_letters_in_each_spot(list_after_third_letter)
    print("FORTH", best_5_letters_to_guess)
    best_letter_4=find_best_letter_to_guess(best_5_letters_to_guess,list_of_letters_guessed)
    item_to_append=list(best_letter_4.values())
    list_of_letters_guessed.append(item_to_append[0])
    list_after_forth_letter=refine_list(best_letter_4,{}, {}, list_after_third_letter)

    # 5th letter
    best_5_letters_to_guess=best_5_letters_in_each_spot(list_after_forth_letter)
    print("FIFTH", best_5_letters_to_guess)
    best_letter_5=find_best_letter_to_guess(best_5_letters_to_guess,list_of_letters_guessed)
    item_to_append=list(best_letter_5.values())
    list_of_letters_guessed.append(item_to_append[0])
    list_after_fifth_letter=refine_list(best_letter_5,{}, {}, list_after_forth_letter)

    print(list_of_letters_guessed)
    print(list_after_fifth_letter)

    return list_after_fifth_letter[0]


guess=make_guess(sample_list)
print(guess)


#%%


# %%
