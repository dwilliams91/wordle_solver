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
    return(best_first, best_second, best_third, best_fourth, best_fifth)


# %%
def refine_list(correct_position_letters, incorrect_position_letters, sample_list):
    remove_list=[]
    remove_list_2=[]
    correct_key_list_position=correct_position_letters.keys()
    incorrect_key_list_position=incorrect_position_letters.keys()
    incorrect_values_list=incorrect_position_letters.values()
    modified_sample_list=sample_list

    if len(correct_position_letters) !=0:
        for x in range(0,len(sample_list)):
            word=sample_list[x]
            need_to_be_removed=False
            # if the right letter is in the right spot
            for position in correct_key_list_position:
                if word[position] != correct_position_letters[position]:
                    need_to_be_removed=True
                    break
            # if the right letter is in the wrong spot, remove words where the letter is in that spot
            for position in incorrect_key_list_position:
                if word[position]==incorrect_key_list_position[position]:
                    need_to_be_removed=True
                    break
            if need_to_be_removed:
                remove_list.append(word)

        for word in remove_list:
            modified_sample_list.remove(word)

    # taking out words that don't contain the letters
    for word in sample_list:
        for letter in incorrect_values_list:
            if letter not in word:
                remove_list_2.append(word)
    
    for word in remove_list_2:
        if word in modified_sample_list:
            modified_sample_list.remove(word)
    
    return modified_sample_list

correct_position_letters_dict={
     
}
incorrect_position_letters={
    2:"t", 
    4:"h"}


refined_list=refine_list(correct_position_letters_dict, incorrect_position_letters, sample_list)


# %%
# best_first, best_second, best_third, best_fourth, best_fifth=solve_worldle(refined_list)
best_letters_to_guess=solve_worldle(sample_list)
best_first, best_second, best_third, best_fourth, best_fifth=best_letters_to_guess
print("best first letter", best_first)
print("best second letter", best_second)
print("best third letter",best_third)
print("best fourth letter",best_fourth)
print("best fifth letter",best_fifth)
# %%

def find_best_word(best_letters_to_guess, sample_list):
    best_letter_for_each_position=[]
    for x in range(0, len(best_letters_to_guess)):
        best_letter_for_each_position.append(best_letters_to_guess[x][0])
    def find_max(list_of_touples):
        occurance_of_letters=[]
        for item in list_of_touples:
            occurance_of_letters.append(item[0])
        occurance_of_letters.sort(reverse=True)
        return occurance_of_letters
# option 1- pick best letter, then 

find_best_word(best_letters_to_guess, sample_list)
# %%
