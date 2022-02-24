

import json
import random
import time
import math
import itertools



class WordleAlgorithm():
    def __init__(self, word_dict, all_possible_combinations):
        self.word_dict=word_dict
        self.original_world_list=list(word_dict.keys())
        self.all_possible_combinations=all_possible_combinations
        


    def refine_list(self, green_letters=None, yellow_letters=None, black_letters=None, my_list=None):
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

    def calculate_colors(self, correct_word, guessed_word):
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
    
    def recalculate_entropy(self, word_list):
        combo_dict=self.calculate_combinations_for_list(word_list, word_list)
        frequency_dict=self.calculate_frequency(combo_dict)
        bit_list=self.calculate_bits_for_list(frequency_dict)
        return bit_list
        

    def calculate_combinations_for_list(self, guess_list, sample_list):
        full_guess_dict={}
        for guess in guess_list:
            full_guess_dict[guess]=[]
        for guess in guess_list:
            for word in sample_list:
                colors_for_guess=[]
                for i in range(0,len(guess)):
                    if guess[i]==word[i]:         
                        colors_for_guess.append(2)
                    elif guess[i] in word and guess[i]!=word[i]:
                        colors_for_guess.append(1)
                    else:
                        colors_for_guess.append(0)
                full_guess_dict[guess].append(str(colors_for_guess))    
        return full_guess_dict

    def CountFrequency(self, my_list): 
        freq = {}
        for item in my_list:
            item=str(item)
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

    def calculate_frequency(self, count_dict):
        return_dictionary={}
        count_dict.keys()
        for word in count_dict.keys():
            return_dictionary[word]=self.CountFrequency(count_dict[word])
        return return_dictionary

    def calculate_bits_for_single_word(self, word, possibility_dict, length):
        possibility_sum=[]
        for combination in self.all_possible_combinations:
            if combination in possibility_dict:
                entropy=math.log2(1/(possibility_dict[combination]/length))
                possibility_sum.append((possibility_dict[combination]/length)*entropy)
        return  sum(possibility_sum)
    
    def calculate_bits_for_list(self, combination_dict):
        bit_dict={}
        for word in list(combination_dict.keys()):
            bit_dict[word]=self.calculate_bits_for_single_word(word, combination_dict[word], len(combination_dict))
        return bit_dict

    def take_turn(self, current_list, goal_word):
        print("my guess is ", current_list[0])
        my_colors=self.calculate_colors(goal_word, current_list[0])
        # print(my_colors)
        refined_list=self.refine_list(my_colors[0], my_colors[1], my_colors[2], current_list)
        recalculated_entropy=self.recalculate_entropy(refined_list)
        print(recalculated_entropy)
        # print(len(refined_list))
        
        
        # print(new_words_in_bit_order)
        

    def play_round(self):
        random_index = random.randint(0,len(self.original_world_list)-1)
        goal_word=self.original_world_list[random_index]
        print("the goal word is ", goal_word)
        self.take_turn(self.original_world_list, goal_word)

def main():
    def get_all_combinations():
        N=5
        possible_values = [0,1,2]
        all_combinations = list(itertools.product(possible_values, repeat=N))
        return_list=[]
        for item in all_combinations:
            item=list(item)
            return_list.append(str(item))
        return return_list

    f=open("total_bits.txt")
    test_string=f.read()
    bits_list = json.loads(test_string)
    sorted_bit_dict={k: v for k, v in sorted(bits_list.items(), key=lambda item: item[1], reverse=True)}


    # my_file = open("full_wordle_list.txt", "r")

    # sample_list = my_file.read()
    # sample_list = sample_list.split(",")

    # words_in_bit_order= list(sorted_bit_list.keys())
    all_combinations=get_all_combinations()


    start_time = time.time()
    instantiate=WordleAlgorithm(word_dict=sorted_bit_dict, all_possible_combinations=all_combinations)
    instantiate.play_round()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()




# def take_turn(current_list, goal_word):
#     # print("my guess is ", current_list[0])
#     my_colors=calculate_colors(goal_word, current_list[0])
#     # print(my_colors)
#     refined_list=refine_list(my_colors[0], my_colors[1], my_colors[2], current_list)
#     # print(len(refined_list))
#     new_bit_dict={}
#     for item in refined_list:
#         new_bit_dict[item]=sorted_bit_list[item]
#     new_sorted_dict={k: v for k, v in sorted(new_bit_dict.items(), key=lambda item: item[1], reverse=True)}
#     new_words_in_bit_order= list(new_sorted_dict.keys())
#     # print(new_words_in_bit_order)
#     return new_words_in_bit_order

# def cal_average(num):
#     sum_num = 0
#     for t in num:
#         sum_num = sum_num + t           

#     avg = sum_num / len(num)
#     return avg

# #%%
# def play_a_round():
#     random_index = random.randint(0,len(sample_list)-1)
#     goal_word=sample_list[random_index]
#     counter=1
#     # print(goal_word)
#     for i in range(0,1):
#         First_Turn=take_turn(words_in_bit_order, goal_word)
#         counter+=1
#         if First_Turn[0]==goal_word:
#             final_guess=First_Turn[0]
#             break
        
#         Second_Turn=take_turn(First_Turn, goal_word)
#         counter+=1
#         if Second_Turn[0]==goal_word:
#             final_guess=Second_Turn[0]
#             break

#         Third_Turn=take_turn(Second_Turn, goal_word)
#         counter+=1
#         if Third_Turn[0]==goal_word:
#             final_guess=Third_Turn[0]
#             break

#         Forth_Turn=take_turn(Third_Turn, goal_word)
#         counter+=1
#         if Forth_Turn[0]==goal_word:
#             final_guess=Forth_Turn[0]
#             break

#         Fifth_Turn=take_turn(Forth_Turn, goal_word)
#         counter+=1
#         final_guess=Fifth_Turn[0]

        
#         if final_guess != goal_word:
#             print(goal_word)
#     # print("your final guess was ", final_guess, " the goal was ", goal_word, ". It took you ", counter, " turns")
#     return counter
    
# random_index = random.randint(0,len(sample_list)-1)
# goal_word=sample_list[random_index]
# print(goal_word)      



# # %%
# def get_data():
#     my_list=[]
#     for i in range(0, 1000):
#         turn=play_a_round()
#         my_list.append(turn)
#     print(cal_average(my_list))
# start_time = time.time()
# get_data()
# print("--- %s seconds ---" % (time.time() - start_time))



