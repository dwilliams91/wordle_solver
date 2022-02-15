#%%
import time
from itertools import permutations


# from sample_wordle import sample_list

my_file = open("wordle_answer.txt", "r")
# my_file = open("large_sample_size.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

my_file = open("full_wordle_list.txt", "r")
full_wordle_guess_list=my_file.read()
full_wordle_guess_list=full_wordle_guess_list.split(",")
def bad_data_finder(sample_list):
    bad_data=[]
    good_data=[]
    for item in sample_list:
        if len(item)==5:
            good_data.append(item)
        else:
            bad_data.append(item)
    return bad_data

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
# %%
start_time = time.time()

def common_elements(test_list):
        res = []
        for i in test_list:
            if i not in res:
                res.append(i)
        res.sort()
        return res
print(len(sample_list))
def elimante_most_words(full_list):
    dict_of_letters=find_best_letter(full_list)
    list_of_letters_in_order=list(dict_of_letters)
    print(list_of_letters_in_order)
    
    remove_list=[]
    best_letters=list_of_letters_in_order[2:7]
    print(best_letters)
    for word in full_list:
        should_break=False
        for letter in best_letters:
            if len(full_list)-len(remove_list)<1:
                should_break=True
                print("dude")
                break
            if letter not in word:
                remove_list.append(word)
                break
        if should_break:
            break
    words_left=(set(full_list)-set(remove_list))
    print(len(words_left))
    print(words_left)


elimante_most_words(sample_list)

print("--- %s seconds ---" % (time.time() - start_time))

# %%

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

def in_guess_list(full_list, word):
    perms = [''.join(p) for p in permutations(word)]

    possible_guesses=[]
    for item in perms:
        item=item[0:5]
        if item in full_list:
            possible_guesses.append(item)
    return possible_guesses


def cal_average(num):
        sum_num = 0
        for t in num:
            sum_num = sum_num + t           

        avg = sum_num / len(num)
        return avg

def what_eliminates_most_words(full_list, guess_list):
    word_dict={}
    for guess_word in guess_list:
        guess_average=[]
        print("--- %s seconds ---" % (time.time() - start_time))
        for target_word in full_list:
            green, yellow, black= calculate_colors(target_word, guess_word)
            after_first_guess=refine_list(green, yellow, black, full_list)
            guess_average.append(len(after_first_guess))
        word_dict[guess_word]=cal_average(guess_average)
    return word_dict

def find_best_second_word(full_answer_list, first_guess, full_guess_list):
    alphabet=["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    my_dictionary={}
    for letter in alphabet:
        my_dictionary[letter]=[]
    guess_average_first=[]

    for target_word in full_answer_list:
        green, yellow, black= calculate_colors(target_word, first_guess)
        after_first_guess=refine_list(green, yellow, black, full_answer_list)
        guess_average_first.append(len(after_first_guess))

        best_letters_after_1=find_best_letter(after_first_guess)
        for letter in alphabet:

            my_dictionary[letter].append(best_letters_after_1[letter])

    for letter in alphabet:
        my_dictionary[letter]=cal_average(my_dictionary[letter])
    sorted_dict={k: v for k, v in sorted(my_dictionary.items(), key=lambda item: item[1], reverse=True)}
    for letter in first_guess:
        del sorted_dict[letter]
    list_of_best_letters_left=list(sorted_dict.keys())
    print(list_of_best_letters_left)
    print(in_guess_list(full_guess_list,list_of_best_letters_left[0:6]))
    return sorted_dict

def what_eliminates_most_words_after_two_rounds(full_list, first_guess, second_guess):
    word_dict={}
    guess_average_first=[]
    guess_average_second=[]

    

    for target_word in full_list:
        green, yellow, black= calculate_colors(target_word, first_guess)
        after_first_guess=refine_list(green, yellow, black, full_list)
        guess_average_first.append(len(after_first_guess))

        # best_letters_after_1=find_best_letter(after_first_guess)
        # for letter in alphabet:

        #     my_dictionary[letter].append(best_letters_after_1[letter])



        green, yellow, black= calculate_colors(target_word, second_guess)
        after_second_guess=refine_list(green, yellow, black, after_first_guess)
        guess_average_second.append(len(after_second_guess))
    # for letter in alphabet:
    #     my_dictionary[letter]=cal_average(my_dictionary[letter])
    # print(my_dictionary)

    word_dict[first_guess]=cal_average(guess_average_first)
    word_dict[second_guess]=cal_average(guess_average_second)
    return word_dict




# %%
start_time = time.time()
guess_list=['bales', 'males', 'cores', 'stern', 'crane', 'rates']
# guess_list=['irate', 'samey', 'rates']
good_guesses={
    "crane":"toils",
    "rates":"noily",
    "bales":"nitro",
    "cores": "laity",
    "irate": 'sonly',
}
# my_word_dict=what_eliminates_most_words(sample_list, guess_list)

first_guess='irate'
second_guess='nouls'
print(what_eliminates_most_words_after_two_rounds(sample_list, first_guess, second_guess))
# print(find_best_second_word(sample_list, first_guess, full_wordle_guess_list))
print("--- %s seconds ---" % (time.time() - start_time))



# %%
# perms = [''.join(p) for p in permutations('stack')]

def in_guess_list(full_list, word):
    perms = [''.join(p) for p in permutations(word)]

    possible_guesses=[]
    for item in perms:
        if item in full_list:
            possible_guesses.append(item)
    return possible_guesses

in_guess_list(full_wordle_guess_list, 'loti')


# %%
