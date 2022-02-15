
import argparse
import time

from numpy import integer
start_time = time.time()
from collections import Counter

# my_file = open("full_wordle_list.txt", "r")

# my_file = open("large_sample_size.txt", "r")
my_file = open("wordle_answer.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")
# from sample_wordle import sample_list
import random

class SolveWordle():
    def __init__(self, sample_list, goal_word=None, turn_number=0, full_letter_count=None, will_print=False, continue_greens=True, first_guess=None, second_guess=None):
        self.sample_list=sample_list
        self.goal_word=goal_word
        self.turn_number=turn_number
        self.full_letter_count=full_letter_count
        self.will_print=will_print
        self.continue_greens=continue_greens
        self.first_guess=first_guess
        self.second_guess=second_guess
    
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
            return sorted_dictionary[0:10]

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
            dictionary_of_all_best_letters=self.full_letter_count[position_of_final_letter]
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
                    # positions
                    
                    # # letter
                    if best_positional_letter[1]>current_best_number and best_positional_letter[0] not in list_of_letters_guessed:
                        current_best_number=best_positional_letter[1]
                        current_best_letter_position=x
                        current_best_letter=best_positional_letter[0]
                

                    # if  best_positional_letter[1]>current_best_number and x not in list_of_positions_guessed:
                    #     current_best_number=best_positional_letter[1]
                    #     current_best_letter_position=x
                    #     current_best_letter=best_positional_letter[0]

                    # item_to_check={x:best_positional_letter[0]}
                    # breakpoint()
                    # if best_positional_letter[1]>current_best_number and item_to_check[x] not in already_guessed_letter[x]:
                    #     current_best_number=best_positional_letter[1]
                    #     current_best_letter_position=x
                    #     current_best_letter=best_positional_letter[0]
        return {
            current_best_letter_position:current_best_letter
        }

    def refine_after_letter_of_guess(self, my_list, dictionary_of_letters_guessed):
        best_5_letters_to_guess=self.best_5_letters_in_each_spot(my_list)
        best_letter_2=self.find_best_letter_to_guess(best_5_letters_to_guess, dictionary_of_letters_guessed)
        dictionary_of_letters_guessed.update(best_letter_2)
        refined_list=self.refine_list(best_letter_2, {}, {}, my_list)
        
        return refined_list, dictionary_of_letters_guessed 

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
        
        if self.continue_greens:
            colors=self.calculate_colors(goal_word, guess)
            list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)
            new_guess=self.make_guess(list_of_words_to_guess)
        else:
            if self.turn_number==1:
                all_black=self.all_black(self.make_guess(self.sample_list))
                list_of_words_to_guess=self.refine_list({}, {}, all_black, self.sample_list)
                if self.second_guess:
                    new_guess=self.second_guess
                else:
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
        if self.goal_word:
            goal_word=self.goal_word
        else:
            goal_word=sample_list[random_index]

        if self.first_guess:
            guess=self.first_guess
        else:
            guess=self.make_guess(self.sample_list)
        
        counter=1
        for i in range(0,1):
            First_Turn=self.take_turn(guess, goal_word, self.sample_list)
            counter+=1
            if First_Turn[0]==First_Turn[1]:
                final_guess=First_Turn[0]
                Second_Turn=False
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
                return counter, First_Turn[0], goal_word, len(Second_Turn[2])
                
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
            #     return counter, len(First_Turn[2]), goal_word
        
        if self.will_print:
            print("you did it! it took you", counter, " turns. the goal was ", goal_word, "your final guess was ", final_guess )
            print("==============================================")
        turn_to_capture=0
        if Second_Turn:
            turn_to_capture=len(Second_Turn[0])
        return counter, First_Turn[0], "" , turn_to_capture
    

def run_test():
    def convert_inputs(my_input):
        if my_input.lower()=='y':
            return True
        elif my_input.lower()=='n':
            return False
        
    def cal_average(num):
        sum_num = 0
        for t in num:
            sum_num = sum_num + t           

        avg = sum_num / len(num)
        return avg

    def common_elements(test_list):
        res = []
        result = sorted(test_list, key = test_list.count,
                                reverse = True)
        for i in result:
            if i not in res:
                res.append(i)
        return res
    
    def find_best_letter_in_given_spot(sample_list, spot):
        alphabet=["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        my_dictionary={}
        for letter in alphabet:
            my_dictionary[letter]=0
        for word in sample_list:
            for x in range(0,len(alphabet)):
                if alphabet[x]==word[spot]:
                    my_dictionary[alphabet[x]]=my_dictionary[alphabet[x]]+1
        my_dictionary=dict(sorted(my_dictionary.items(), key=lambda item: item[1], reverse=True))
        return my_dictionary

    list_of_best_positional_letters=[]
    for i in range(0,5):
        list_of_best_positional_letters.append(find_best_letter_in_given_spot(sample_list, i))
    
    list_of_turns=[]
    second_guesses=[]
    failed_words=[]
    list_after_first_guess=[]

    continue_greens= convert_inputs(input("continue greens for second word?(y/n) "))
    will_print= convert_inputs(input("print each round?(y/n) "))

    goal_word= input("specific goal word? ")
    first_guess=input("specific first word? ")
    second_guess=input("specific second word? ")
    full_diagnostic= convert_inputs(input("Full diagnostic?((y/n)) "))

    if full_diagnostic==False:
        number_of_tests=int(input("number of tests "))
    else:
        number_of_tests=len(sample_list)
    
    for i in range(0, number_of_tests):
        if full_diagnostic:
            goal_word=sample_list[i]
        count, my_second_guess, final_guess, length_after_first_guess =SolveWordle(sample_list, goal_word=goal_word, full_letter_count=list_of_best_positional_letters, will_print=will_print, continue_greens=continue_greens, first_guess=first_guess, second_guess=second_guess).play_a_round()
        list_of_turns.append(count)
        second_guesses.append(my_second_guess)
        if final_guess:
            failed_words.append(final_guess)
        list_after_first_guess.append(length_after_first_guess)

    if continue_greens:
        print("when it DOES keep greens or yellows it took", cal_average(list_of_turns), " turns to get it right")
    else:
        print("when it DOESN'T keep greens or yellows it took", cal_average(list_of_turns), " turns to get it right")
    # print("It's second guess was  ", common_elements(second_guesses))
    print("it failed to get it ", len(failed_words), " times")
    # print("it couldn't guess", common_elements(failed_words))
    print("after the second word, there were an average of ", cal_average(list_after_first_guess))
    print("--- %s seconds ---" % (time.time() - start_time))



def main():
    run_test()

   

if __name__ == "__main__":
    main()
    # print("--- %s seconds ---" % (time.time() - start_time))
