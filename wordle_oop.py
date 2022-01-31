#%%
my_file = open("large_sample_size.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split(",")

import random
#%%

class SolveWordle():
    def __init__(self, sample_list):
        self.sample_list=sample_list
    
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
    def letter_of_guess(self, my_list, list_of_letters_guessed):

        best_5_letters_to_guess=self.best_5_letters_in_each_spot(my_list)
        # print(" letter distrubtion ", best_5_letters_to_guess)
        best_letter_2=self.find_best_letter_to_guess(best_5_letters_to_guess, list_of_letters_guessed)
        # print("best letter", best_letter_2)
        item_to_append=list(best_letter_2.values())
        list_of_letters_guessed.append(item_to_append[0])
        refined_list=self.refine_list(best_letter_2, {}, {}, my_list)
        # print("current_state_of_list", refined_list)
        # if len(refined_list)==0:
        return refined_list, list_of_letters_guessed

    def make_guess(self, list_of_words):
    # initial list
        list_of_letters_guessed=[]
        my_guess=[]
        list_after_first_letter, list_of_letters_guessed=self.letter_of_guess(list_of_words, list_of_letters_guessed)
        if len(list_after_first_letter)<=1:
            # print("using 1 letter to guess")
            my_guess=list_after_first_letter[0]

        list_after_second_letter, list_of_letters_guessed=self.letter_of_guess(list_after_first_letter, list_of_letters_guessed)
        if len(list_after_second_letter)<=1:
            # print("using 2 letters to guess")
            my_guess=list_after_second_letter[0]

        list_after_third_letter, list_of_letters_guessed=self.letter_of_guess(list_after_second_letter, list_of_letters_guessed)
        if len(list_after_third_letter)<=1:
            # print("using 3 letters to guess")
            my_guess=list_after_third_letter[0]

        list_after_forth_letter, list_of_letters_guessed=self.letter_of_guess(list_after_third_letter, list_of_letters_guessed)
        if len(list_after_forth_letter)<=1:
            # print("using 4 letters to guess")
            my_guess=list_after_forth_letter[0]
            return my_guess

        list_after_fifth_letter, list_of_letters_guessed=self.letter_of_guess(list_after_forth_letter, list_of_letters_guessed)
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
        if correct_word==guessed_word:
            print("YOU DID IT")
            print("The word is ", guessed_word)
        
        return green_dict, yellow_dict, black_dict

    def take_turn(self, guess, goal_word, current_word_list):
        print("my guess is ", guess)
        print("the goal word is ", goal_word)

        colors=self.calculate_colors(goal_word, guess)
        print("green", colors[0])
        print("yellow", colors[1])
        print("black", colors[2])

        list_of_words_to_guess=self.refine_list(colors[0], colors[1], colors[2], current_word_list)
        print("there are ", len(list_of_words_to_guess), " words left")

        print("this is the list of words ",list_of_words_to_guess)

        new_guess=self.make_guess(list_of_words_to_guess)
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
        goal_word=self.sample_list[random_index]
        # print("the goal word is", goal_word)
        guess=self.make_guess(self.sample_list)
        # print("the first guess is ", guess)

        for i in range(0,1):
            First_Turn=self.take_turn(guess, goal_word, self.sample_list)
            if First_Turn[0]==First_Turn[1]:
                final_guess=First_Turn[0]
                break
            Second_Turn=self.take_turn(First_Turn[0], First_Turn[1], First_Turn[2])
            if Second_Turn[0]==Second_Turn[1]:
                final_guess=Second_Turn[0]
                break
            Third_Turn=self.take_turn(Second_Turn[0], Second_Turn[1], Second_Turn[2])
            if Third_Turn[0]==Third_Turn[1]:
                final_guess=Third_Turn[0]
                break
            Forth_Turn=self.take_turn(Third_Turn[0], Third_Turn[1], Third_Turn[2])
            if Forth_Turn[0]==Forth_Turn[1]:
                final_guess=Forth_Turn[0]
                break
            Fifth_Turn=self.take_turn(Forth_Turn[0], Forth_Turn[1], Forth_Turn[2])
            if Fifth_Turn[0]==Fifth_Turn[1]:
                final_guess=Fifth_Turn[0]
                break
            else:
                final_guess=Fifth_Turn[0]
                print("YOU FAILED the goal was ", goal_word, "your final guess was ", final_guess )
        print("you did it! the goal was ", goal_word, "your final guess was ", final_guess )
        print("==============================================")
# %%