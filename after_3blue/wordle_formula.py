#%%

my_file = open("full_wordle_list.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

import json
import random
import time

f=open("total_bits.txt")
test_string=f.read()
bits_list = json.loads(test_string)
sorted_bit_list={k: v for k, v in sorted(bits_list.items(), key=lambda item: item[1], reverse=True)}
 
words_in_bit_order= list(sorted_bit_list.keys())

start_time = time.time()
random_index = random.randint(0,len(sample_list)-1)
goal_word=sample_list[random_index]
print(goal_word)

def refine_list(green_letters=None, yellow_letters=None, black_letters=None, my_list=None):
    green_remove_list=[]
    yellow_remove_list=[]
    black_remove_list=[]

    correct_key_list_position=list(green_letters.keys())
    incorrect_key_list_position=list(yellow_letters.keys())
    incorrect_values_list=yellow_letters.values()
    black_letters_list=black_letters.values()

    # if len(green_letters) !=0:
    for x in range(0,len(my_list)):
        word=my_list[x]
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
    remove_not_greens=(set(my_list)-set(green_remove_list))

    # taking out words that don't contain the letters 
    for word in my_list:
        for letter in incorrect_values_list:
            
            if letter not in word:
                yellow_remove_list.append(word)
    
    remove_not_yellow=(set(remove_not_greens)-set(yellow_remove_list))


    # #take out words that dont have black letters
    for x in range(0,len(my_list)):
        word=my_list[x]
        for letter in word:
            if letter in black_letters_list:
                black_remove_list.append(word)
    
    remove_black_letters=(set(remove_not_yellow)-set(black_remove_list))


    
    return list(remove_black_letters)

def calculate_colors(correct_word, guessed_word):
    green_dict={}
    yellow_dict={}
    black_dict={}

    for i in range(0, len(correct_word)):
        if guessed_word[i]==correct_word[i]:
            green_dict[i]=guessed_word[i]
            continue
        elif guessed_word[i] in correct_word:
            yellow_dict[i]=guessed_word[i]
            continue
        else:
            black_dict[i]=guessed_word[i]
    return green_dict, yellow_dict, black_dict



# %%


def take_turn(current_list, goal_word):
    print("my guess is ", current_list[0])
    my_colors=calculate_colors(goal_word, current_list[0])
    print(my_colors)
    refined_list=refine_list(my_colors[0], my_colors[1], my_colors[2], current_list)
    print(len(refined_list))
    new_bit_dict={}
    for item in refined_list:
        new_bit_dict[item]=sorted_bit_list[item]
    new_sorted_dict={k: v for k, v in sorted(new_bit_dict.items(), key=lambda item: item[1], reverse=True)}
    new_words_in_bit_order= list(new_sorted_dict.keys())
    print(new_words_in_bit_order)
    return new_words_in_bit_order

list_after_first_turn=take_turn(words_in_bit_order, goal_word)
#%%
list_after_second_turn=take_turn(list_after_first_turn, goal_word)

# %%
list_after_third_turn=take_turn(list_after_second_turn, goal_word)



# %%
