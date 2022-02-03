
import argparse

from numpy import False_

my_file = open("large_sample_size.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split(",")

import random

class SolveWordle():
    def __init__(self, sample_list, turn_number=0, full_letter_count=None, will_print=False, continue_greens=True):
        self.sample_list=sample_list
        self.turn_number=turn_number
        self.full_letter_count=full_letter_count
        self.will_print=will_print
        self.continue_greens=continue_greens
    
    def find_best_letter(self, sample_list):
        alphabet=["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        my_dictionary={}
        for letter in alphabet:
            my_dictionary[letter]=0
        for word in sample_list:
            for x in range(0,len(alphabet)):
                if alphabet[x] in word:
                    my_dictionary[alphabet[x]]=my_dictionary[alphabet[x]]+1
        my_dictionary=dict(sorted(my_dictionary.items(), key=lambda item: item[1], reverse=True))
        return my_dictionary
    
    def best_5_letters_in_each_spot(self, sample_list):
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


    def find_best_letter_to_guess(self, best_letters_to_guess, already_guessed_letter):
        current_best_number=0
        current_best_letter_position=0
        current_best_letter=""
        list_of_letters_guessed=list(already_guessed_letter.values())
        list_of_positions_guessed=list(already_guessed_letter.keys())

        possible_positions=[0,1,2,3,4]
        if len(list_of_letters_guessed)==4:
            for item in possible_positions:
                if item not in list_of_positions_guessed:
                    position_of_final_letter=item
            list_of_best_final_position=best_letters_to_guess[position_of_final_letter]
            just_the_letters_of_final_position=[]
            for x in range(0,5):
                if list_of_best_final_position[x][1] !=0:
                    just_the_letters_of_final_position.append(list_of_best_final_position[x][0])
            dictionary_of_all_best_letters=self.full_letter_count
            counts_of_final_letters={}
            for letter in just_the_letters_of_final_position:
                    counts_of_final_letters[letter]=dictionary_of_all_best_letters[letter]
            largest_count=max(counts_of_final_letters.values())
            current_best_letter=list(counts_of_final_letters.keys())[list(counts_of_final_letters.values()).index(largest_count)]
            current_best_letter_position=position_of_final_letter
        else:
            for x in range(0,len(best_letters_to_guess)):
                for i in range(0,4):
                    item=best_letters_to_guess[x]
                    best_positional_letter=item[i]   

                    if best_positional_letter[1]>current_best_number and best_positional_letter[0] not in list_of_letters_guessed:
                        current_best_number=best_positional_letter[1]
                        current_best_letter_position=x
                        current_best_letter=best_positional_letter[0]
        return {
            current_best_letter_position:current_best_letter
        }

    def refine_after_letter_of_guess(self, my_list, dictionary_of_letters_guessed):
        # print(my_list)
        best_5_letters_to_guess=self.best_5_letters_in_each_spot(my_list)
        best_letter_2=self.find_best_letter_to_guess(best_5_letters_to_guess, dictionary_of_letters_guessed)
        dictionary_of_letters_guessed.update(best_letter_2)
        refined_list=self.refine_list(best_letter_2, {}, {}, my_list)

        return refined_list, dictionary_of_letters_guessed 
    # def find_best_letter_to_guess(self, best_letters_to_guess, already_guessed_letter):
    #     current_best_number=0
    #     current_best_letter_position=0
    #     current_best_letter=""

    #     for x in range(0,len(best_letters_to_guess)):
    #         for i in range(0,4):
    #             item=best_letters_to_guess[x]
    #             best_positional_letter=item[i]   
    #             # print(best_positional_letter," is compared to ('", current_best_letter, "', ", current_best_number)

    #             if best_positional_letter[1]>current_best_number and best_positional_letter[0] not in already_guessed_letter:
    #                 current_best_number=best_positional_letter[1]
    #                 current_best_letter_position=x
    #                 current_best_letter=best_positional_letter[0]
    #     return {
    #         current_best_letter_position:current_best_letter
    # }
    # def letter_of_guess(self, my_list, list_of_letters_guessed):

    #     best_5_letters_to_guess=self.best_5_letters_in_each_spot(my_list)
    #     # print(" letter distrubtion ", best_5_letters_to_guess)
    #     best_letter_2=self.find_best_letter_to_guess(best_5_letters_to_guess, list_of_letters_guessed)
    #     # print("best letter", best_letter_2)
    #     item_to_append=list(best_letter_2.values())
    #     list_of_letters_guessed.append(item_to_append[0])
    #     refined_list=self.refine_list(best_letter_2, {}, {}, my_list)
    #     # print("current_state_of_list", refined_list)
    #     # if len(refined_list)==0:
    #     return refined_list, list_of_letters_guessed

    def make_guess(self, list_of_words):
    # initial list
        list_of_letters_guessed={}
        my_guess=[]
        list_after_first_letter, list_of_letters_guessed=self.refine_after_letter_of_guess(list_of_words, list_of_letters_guessed)
        if len(list_after_first_letter)<=1:
            # print("using 1 letter to guess")
            my_guess=list_after_first_letter[0]
            return my_guess


        list_after_second_letter, list_of_letters_guessed=self.refine_after_letter_of_guess(list_after_first_letter, list_of_letters_guessed)
        if len(list_after_second_letter)<=1:
            # print("using 2 letters to guess")
            my_guess=list_after_second_letter[0]
            return my_guess


        list_after_third_letter, list_of_letters_guessed=self.refine_after_letter_of_guess(list_after_second_letter, list_of_letters_guessed)
        if len(list_after_third_letter)<=1:
            if len(list_after_third_letter)==0:
                my_guess=list_after_second_letter[0]
            else:
                my_guess=list_after_second_letter[0]
            return my_guess


        list_after_forth_letter, list_of_letters_guessed=self.refine_after_letter_of_guess(list_after_third_letter, list_of_letters_guessed)
        if len(list_after_forth_letter)<=1:
            if len(list_after_forth_letter)==0:
                my_guess=list_after_third_letter[0]
            else:
                my_guess=list_after_forth_letter[0]
            return my_guess

        list_after_fifth_letter, list_of_letters_guessed=self.refine_after_letter_of_guess(list_after_forth_letter, list_of_letters_guessed)
        if len(list_after_fifth_letter)<=1:
            # print("using 5 letters to guess")
            my_guess=list_after_fifth_letter[0]
        return my_guess

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
        # print("green", green_dict)
        # print("yellow", yellow_dict)
        # print("black", black_dict)
        if correct_word==guessed_word and self.will_print:
            print("YOU DID IT")
            print("The word is ", guessed_word)
        
        return green_dict, yellow_dict, black_dict
    
    def all_black(self, word):
        my_dict={}
        for i in range(0,len(word)):
            my_dict[i]=word[i]
        return my_dict

    def take_turn(self, guess, goal_word, current_word_list):
        self.turn_number+=1
        # print("turn", self.turn_number)
        # print("my guess is ", guess)
        # print("the goal word is ", goal_word)

        # colors=self.calculate_colors(goal_word, guess)
        # print("green", colors[0])
        # print("yellow", colors[1])
        # print("black", colors[2])

        
        # list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)

        # print("there are ", len(list_of_words_to_guess), " words left")

        # print("this is the list of words ",list_of_words_to_guess)
        if self.continue_greens:
            colors=self.calculate_colors(goal_word, guess)
            list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)
            new_guess=self.make_guess(list_of_words_to_guess)
        else:
            if self.turn_number==1:
                all_black=self.all_black(self.make_guess(self.sample_list))
                list_of_words_to_guess=self.refine_list({}, {}, all_black, self.sample_list)
                new_guess=self.make_guess(list_of_words_to_guess)
                colors=self.calculate_colors(goal_word, guess)
                list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)
            else:
                colors=self.calculate_colors(goal_word, guess)
                list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)
                new_guess=self.make_guess(list_of_words_to_guess)

        if self.will_print:
            print("turn", self.turn_number)
            print("my guess is ", guess)
            print("the goal word is ", goal_word)
            print("green", colors[0])
            print("yellow", colors[1])
            print("black", colors[2])
            print("there are ", len(list_of_words_to_guess), " words left")
            print("this is the list of words ",list_of_words_to_guess)


            print("my new guess is ", new_guess)
            print("_______________________________________________________________________")

        # while (new_guess != goal_word):
        #     print("dude")
        #     breakpoint()
        #     self.take_turn(new_guess, goal_word, list_of_words_to_guess)

        
        return new_guess, goal_word, list_of_words_to_guess

    def type_outcome_faster(self, my_word):
        green_dict={}
        yellow_dict={}
        black_dict={}
        for i in range(0,5):
            if list(my_word[i].keys())[0]=='g':
                green_dict[i]=list(my_word[i].values())[0]
            elif list(my_word[i].keys())[0]=='y':
                yellow_dict[i]=list(my_word[i].values())[0]
            elif list(my_word[i].keys())[0]=='b':
                black_dict[i]=list(my_word[i].values())[0]

        return green_dict, yellow_dict, black_dict

    def play_a_round(self):
        random_index = random.randint(0,len(self.sample_list)-1)
        goal_word=self.sample_list[random_index]
        # goal_word='toper'
        # print("the goal word is", goal_word)
        guess=self.make_guess(self.sample_list)
        # print("the first guess is ", guess)
        counter=1
        for i in range(0,1):
            First_Turn=self.take_turn(guess, goal_word, self.sample_list)
            counter+=1
            if First_Turn[0]==First_Turn[1]:
                final_guess=First_Turn[0]
                break 
            Second_Turn=self.take_turn(First_Turn[0], First_Turn[1], First_Turn[2])
            counter+=1

            if Second_Turn[0]==Second_Turn[1]:
                final_guess=Second_Turn[0]
                break
            Third_Turn=self.take_turn(Second_Turn[0], Second_Turn[1], Second_Turn[2])
            counter+=1

            if Third_Turn[0]==Third_Turn[1]:
                final_guess=Third_Turn[0]
                break
            Forth_Turn=self.take_turn(Third_Turn[0], Third_Turn[1], Third_Turn[2])
            counter+=1

            if Forth_Turn[0]==Forth_Turn[1]:
                final_guess=Forth_Turn[0]
                break
            Fifth_Turn=self.take_turn(Forth_Turn[0], Forth_Turn[1], Forth_Turn[2])
            counter+=1

            if Fifth_Turn[0]==Fifth_Turn[1]:
                final_guess=Fifth_Turn[0]
                break
            else:
                final_guess=Fifth_Turn[0]
                final_guess=Fifth_Turn[0]
                if self.will_print:
                    print("YOU FAILED the goal was ", goal_word, "your final guess was ", final_guess )
                return counter, goal_word
                
            # SixthTurn=self.take_turn(Fifth_Turn[0], Fifth_Turn[1], Fifth_Turn[2])
            # counter+=1
            # if SixthTurn[0]==SixthTurn[1]:
            #     final_guess=SixthTurn[0]
            #     break
            # else:
            #     final_guess=SixthTurn[0]
            #     final_guess=Fifth_Turn[0]
            #     if self.will_print:
            #         print("YOU FAILED the goal was ", goal_word, "your final guess was ", final_guess )
            #     return counter, First_Turn[0], goal_word
        if self.will_print:
            print("you did it! it took you", counter, " turns. the goal was ", goal_word, "your final guess was ", final_guess )
            print("==============================================")
        return counter, ""

def main():
    def cal_average(num):
        sum_num = 0
        for t in num:
            sum_num = sum_num + t           

        avg = sum_num / len(num)
        return avg

    def common_elements(test_list):
        res = []
        for i in test_list:
            if i not in res:
                res.append(i)
        res.sort()
        return res

    def find_best_letter(sample_list):
        alphabet=["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        my_dictionary={}
        for letter in alphabet:
            my_dictionary[letter]=0
        for word in sample_list:
            for x in range(0,len(alphabet)):
                if alphabet[x] in word:
                    my_dictionary[alphabet[x]]=my_dictionary[alphabet[x]]+1
        my_dictionary=dict(sorted(my_dictionary.items(), key=lambda item: item[1], reverse=True))
        return my_dictionary

    full_letter_count=find_best_letter(sample_list)
    list_of_turns=[]
    failed_words=[]
    for i in range(0,100):
        count, final_guess=SolveWordle(sample_list, full_letter_count=full_letter_count, will_print=False, continue_greens=False).play_a_round()
        list_of_turns.append(count)
        if final_guess:
            failed_words.append(final_guess)
    print("it took", cal_average(list_of_turns))
    print("it failed to get it ", len(failed_words), " times")
    print("it couldn't guess", common_elements(failed_words))
    

if __name__ == "__main__":
    main()