"""sum(p(x))*log2(1/p(x))"""
# %%
import time

my_file = open("large_sample_size.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

import math


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
#%%
start_time = time.time()
guess_list=['bales', 'males', 'cores', 'stern', 'crane', 'rates']




print("--- %s seconds ---" % (time.time() - start_time))


# %%
def formula(x):
    return math.log(1/x,2)

print(formula(8))
# %%
import itertools
N = 5 # number of objects (e.g. slots)
possible_values = [0,1,2]

my_result = list(itertools.product(possible_values, repeat=N))

print(my_result)

    
# %%
my_file = open("large_sample_size.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")
import time

import itertools
from collections import Counter
from itertools import chain

N = 5 # number of objects (e.g. slots)
possible_values = [0,1,2]

my_result = list(itertools.product(possible_values, repeat=N))

guess_list=['bales', 'males', 'cores', 'stern', 'crane', 'rates']
# sample_list=["hello", "telod", "hello", "baldy"]
def calculate_counts_for_entropy(guess_list, sample_list):
    
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
            full_guess_dict[guess].append(colors_for_guess)    

    return full_guess_dict

def CountFrequency(my_list):
 
    # Creating an empty dictionary
    freq = {}
    for item in my_list:
        item=str(item)
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def calculate_entropy(count_dict):
    return_dictionary={}
    count_dict.keys()
    for word in count_dict.keys():
        
        return_dictionary[word]=CountFrequency(count_dict[word])

    
    return return_dictionary




start_time = time.time()    

count=calculate_counts_for_entropy(sample_list, sample_list)
entropy=calculate_entropy(count)
print("--- %s seconds ---" % (time.time() - start_time))


# %%
import json

# json.dumps(entropy)
# f=open("calculated_entropy.txt", "a")
# f.write(str(entropy))
# f.close()

# print("done")
# START HERE
# %%
import json
from ast import literal_eval
import itertools

f=open("calculated_entropy.txt")
test_string=f.read()
pulled_entropy = json.loads(test_string)
# print(type(res))
#%%
N = 5 # number of objects (e.g. slots)
possible_values = [0,1,2]

all_combinations = list(itertools.product(possible_values, repeat=N))
def fix_combinations(list_of_sets):
    return_list=[]
    for item in list_of_sets:
        item=list(item)
        return_list.append(str(item))
    return return_list
all_combinations=fix_combinations(all_combinations)

# list(res['bales'])[0]
# print(type(my_array))
# dude=literal_eval(my_array)
# %%
# how probable is it-- entropy['bales'][pattern]
import math

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

def log_formula(x):
    return math.log(1/x,2)

def final_formula(word, probability_list, combinations):
    empty_sum=[]
    word_combination=probability_list[word]
    for combination in combinations:
        if combination in list(word_combination.keys()):
            empty_sum.append(word_combination[combination]/5700)
            # entropy=log_formula(word_combination[combination]/5700)
            # empty_sum.append(entropy)
    return empty_sum


word='ovals'
final_formula(word, pulled_entropy, all_combinations)

# %%
