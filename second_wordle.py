#%%
import time

# from sample_wordle import sample_list

my_file = open("full_wordle_list.txt", "r")
# my_file = open("large_sample_size.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

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
#%%
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

# %%
start_time = time.time()
# guess_list=['bales', 'males', 'cores', 'stern', 'crane']
guess_list=['irate', 'samey', 'rates']
my_word_dict=what_eliminates_most_words(sample_list, guess_list)
print("--- %s seconds ---" % (time.time() - start_time))

    # %%
