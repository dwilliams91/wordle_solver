
"""HIT RUN ON THE FIRST CELL TO DEFINE ALL THE FUNCTIONS"""

#%%
my_file = open("full_wordle_list.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split(",")

import random

#%%
import random

my_file = open("wordle_answer.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split(",")
# this returns a 5X5 list of the 5 most common letter in each spot
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
        return sorted_dictionary[0:10]

    best_first=find_top_5(letter_dictionary_first)
    best_second=find_top_5(letter_dictionary_second)
    best_third=find_top_5(letter_dictionary_third)
    best_fourth=find_top_5(letter_dictionary_fourth)
    best_fifth=find_top_5(letter_dictionary_fifth)
    return [best_first, best_second, best_third, best_fourth, best_fifth]


first_round=best_5_letters_in_each_spot(sample_list)
print(first_round[0])
print(first_round[1])
print(first_round[2])
print(first_round[3])
print(first_round[4])

def all_black(word):
        my_dict={}
        for i in range(0,len(word)):
            my_dict[i]=word[i]
        return my_dict

# this refines the list depending on the guess. 
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

# sample data
correct_position_letters_dict={
   3: 'e'
}
incorrect_position_letters={
    0: 'b',
}
incorrect_letters={
   1: 'a',
    2: 'l', 
    4: 's'
}

# testing_1=refine_list(correct_position_letters_dict, incorrect_position_letters, incorrect_letters, sample_list )
# print(testing_1)

# this looks through the top 5X5 list, and finds the best letter
def find_best_letter_to_guess(best_letters_to_guess, already_guessed_letter):
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
        for x in range(0,10):
            if list_of_best_final_position[x][1] !=0:

                just_the_letters_of_final_position.append(list_of_best_final_position[x][0])
        dictionary_of_all_best_letters=find_best_letter(sample_list)
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

def refine_after_letter_of_guess(my_list, dictionary_of_letters_guessed):
    # print(my_list)
    best_5_letters_to_guess=best_5_letters_in_each_spot(my_list)
    best_letter_2=find_best_letter_to_guess(best_5_letters_to_guess, dictionary_of_letters_guessed)
    dictionary_of_letters_guessed.update(best_letter_2)
    refined_list=refine_list(best_letter_2, {}, {}, my_list)

    return refined_list, dictionary_of_letters_guessed 

def make_guess(list_of_words):
    # initial list
    list_of_letters_guessed={}
    my_guess=[]
    list_after_first_letter, list_of_letters_guessed=refine_after_letter_of_guess(list_of_words, list_of_letters_guessed)
    if len(list_after_first_letter)<=1:
        # print("using 1 letter to guess")
        my_guess=list_after_first_letter[0]

    list_after_second_letter, list_of_letters_guessed=refine_after_letter_of_guess(list_after_first_letter, list_of_letters_guessed)
    if len(list_after_second_letter)<=1:
        # print("using 2 letters to guess")
        my_guess=list_after_second_letter[0]

    list_after_third_letter, list_of_letters_guessed=refine_after_letter_of_guess(list_after_second_letter, list_of_letters_guessed)
    if len(list_after_third_letter)<=1:
        # print("using 3 letters to guess")
        my_guess=list_after_third_letter[0]

    list_after_forth_letter, list_of_letters_guessed=refine_after_letter_of_guess(list_after_third_letter, list_of_letters_guessed)
    if len(list_after_forth_letter)<=1:
        # print("using 4 letters to guess")
        my_guess=list_after_forth_letter[0]
        return my_guess

    list_after_fifth_letter, list_of_letters_guessed=refine_after_letter_of_guess(list_after_forth_letter, list_of_letters_guessed)
    if len(list_after_fifth_letter)<=1:
        # print("using 5 letters to guess")
        my_guess=list_after_fifth_letter[0]
    return my_guess



def make_guess_recursive(list_of_words,  dictionary_of_letters_guessed):
    list_of_letters_guessed=list(dictionary_of_letters_guessed)
    if len(list_of_words)>1 and len(list_of_letters_guessed)<4:
        list_after_turn, list_of_letters_guessed=refine_after_letter_of_guess(list_of_words, dictionary_of_letters_guessed)
        make_guess_recursive(list_after_turn, dictionary_of_letters_guessed)
    elif len(list_of_letters_guessed)==4:
        # print(dictionary_of_letters_guessed)
        print(best_5_letters_in_each_spot(list_of_words))
        print("is this hitting")
        return list_of_words
    else: 
        print(list_of_words)
        return list_of_words


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
    # print("green", green_dict)
    # print("yellow", yellow_dict)
    # print("black", black_dict)
    if correct_word==guessed_word:
        print("YOU DID IT")
        print("The word is ", guessed_word)
    
    return green_dict, yellow_dict, black_dict

def take_turn(guess, goal_word, current_word_list):
    print("my guess is ", guess)
    print("the goal word is ", goal_word)

    colors=calculate_colors(goal_word, guess)
    print("green", colors[0])
    print("yellow", colors[1])
    print("black", colors[2])

    list_of_words_to_guess=refine_list(colors[0], colors[1], colors[2], current_word_list)
    print("there are ", len(list_of_words_to_guess), " words left")

    print("this is the list of words ",list_of_words_to_guess)

    new_guess=make_guess(list_of_words_to_guess)
    print("my new guess is ", new_guess)
    print("_______________________________________________________________________")
    return new_guess, goal_word, list_of_words_to_guess

def type_outcome_faster(my_word):
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



# %%
"""HIT RUN CELL TO HAVE THE ALGORTHM PLAY ITSELF"""
def play_a_round(sample_list):
    random_index = random.randint(0,len(sample_list)-1)
    goal_word=sample_list[random_index]
    # print("the goal word is", goal_word)
    guess=make_guess(sample_list)
    # print("the first guess is ", guess)

    for i in range(0,1):
        First_Turn=take_turn(guess, goal_word, sample_list)
        if First_Turn[0]==First_Turn[1]:
            final_guess=First_Turn[0]
            break
        Second_Turn=take_turn(First_Turn[0], First_Turn[1], First_Turn[2])
        if Second_Turn[0]==Second_Turn[1]:
            final_guess=Second_Turn[0]
            break
        Third_Turn=take_turn(Second_Turn[0], Second_Turn[1], Second_Turn[2])
        if Third_Turn[0]==Third_Turn[1]:
            final_guess=Third_Turn[0]
            break
        Forth_Turn=take_turn(Third_Turn[0], Third_Turn[1], Third_Turn[2])
        if Forth_Turn[0]==Forth_Turn[1]:
            final_guess=Forth_Turn[0]
            break
        Fifth_Turn=take_turn(Forth_Turn[0], Forth_Turn[1], Forth_Turn[2])
        if Fifth_Turn[0]==Fifth_Turn[1]:
            final_guess=Fifth_Turn[0]
            break
        else:
            final_guess=Fifth_Turn[0]
            print("YOU FAILED the goal was ", goal_word, "your final guess was ", final_guess )
    print("you did it! the goal was ", goal_word, "your final guess was ", final_guess )
    print("==============================================")
play_a_round(sample_list)
# _______________________________________________________________________________________________________________________________________











# %%

"""
results_after_guess=[
#     {"b":"b"},
#     {"b":"a"},
#     {"b":"l"},
#     {"b":"e"},
#     {"b":"s"}
# ]
THE KEYS SHOULD EITHER BE 
"g" FOR GREEN, 
"y" FOR YELLOW
"b" FOR BLACK

THE VALUES ARE THE LETTERS OF YOUR GUESS IN ORDER
"""


results_after_guess=[
    {"g":"c"},
    {"b":"r"},
    {"y":"a"},
    {"b":"n"},
    {"b":"e"}
]
turn_1_results=type_outcome_faster(results_after_guess)
print(turn_1_results[0])
print(turn_1_results[1])
print(turn_1_results[2])
turn_1=refine_list(turn_1_results[0], turn_1_results[1], turn_1_results[2], sample_list )
print(turn_1)
make_guess(turn_1)
# %%
results_after_guess=[
    {"g":"t"},
    {"b":"t"},
    {"g":"a"},
    {"g":"r"},
    {"b":"k"}
]
turn_2_results=type_outcome_faster(results_after_guess)

turn_2=refine_list(turn_2_results[0], turn_2_results[1], turn_2_results[2], turn_1)
print(turn_2)
make_guess(turn_2)
# %%
results_after_guess=[
    {"g":"s"},
    {"b":"c"},
    {"g":"a"},
    {"g":"r"},
    {"b":"p"}
]
turn_3_results=type_outcome_faster(results_after_guess)

turn_3=refine_list(turn_3_results[0], turn_3_results[1], turn_3_results[2], turn_2 )
print(turn_3)
make_guess(turn_3)
# %%
results_after_guess=[
    {"g":"s"},
    {"b":"m"},
    {"b":"i"},
    {"y":"t"},
    {"g":"e"}
]
turn_4_results=type_outcome_faster(results_after_guess)

turn_4=refine_list(turn_4_results[0], turn_4_results[1], turn_4_results[2], turn_3 )
print(turn_4)
make_guess(turn_4)

# %%
results_after_guess=[
    {"b":"u"},
    {"b":"n"},
    {"b":"f"},
    {"b":"e"},
    {"b":"d"}
]
turn_5_results=type_outcome_faster(results_after_guess)

turn_5=refine_list(turn_5_results[0], turn_5_results[1], turn_5_results[2], turn_4 )
print(turn_5)
make_guess(turn_5)

#%%
i=0
while i<5:
    print(i)
    i+=1
# %%
second_guesses= ['abler', 'acres', 'aimer', 'airer', 'amino', 'bally', 'belch', 'blame', 'blare', 'bless', 'bract', 'brass', 'calve', 'carry', 'carte', 'clots', 'cocks', 'corky', 'false', 'flats', 'flour', 'folly', 'gamer', 'gamin', 'golem', 'grate', 'homer', 'humpy', 'lamer', 'lapse', 'later', 'lawny', 'lilts', 'limos', 'local', 'loses', 'mains', 'malts', 'mango', 'manly', 'mares', 'marge', 'mashy', 'masse', 'mater', 'melon', 'melts', 'menus', 'merry', 'mesne', 'miler', 'mires', 'miter', 'molar', 'moles', 'molly', 'molts', 'monad', 'moral', 'morel', 'mosts', 'mothy', 'mussy', 'nails', 'nares', 'nears', 'oiler', 'pales', 'palmy', 'parer', 'pelts', 'pilau', 'plump', 'ramps', 'relay', 'rents', 'riles', 'roble', 'rower', 'rumps', 'saner', 'scalp', 'seals', 'seams', 'sheer', 'shell', 'shlep', 'sines', 'slams', 'slate', 'slier', 'slimy', 'smirk', 'smote', 'spilt', 'spire', 'splat', 'stamp', 'stare', 'stark', 'stout', 'table', 'talks', 'tarts', 'taste', 'tasty', 'tempo', 'terms', 'tomes', 'towel', 'trams', 'trite']

print(len(second_guesses))
# %%
print(find_best_letter(sample_list))
# %%
