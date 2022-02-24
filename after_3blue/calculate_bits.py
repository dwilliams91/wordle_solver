import json
import itertools
import math


f=open("full_calculated_possibilities.txt")
test_string=f.read()
possibility_list = json.loads(test_string)

my_file = open("full_wordle_list.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

class CalculateBits():
    def __init__(self, word=None, possibility_list=possibility_list, all_combinations=None):
        self.word=word
        self.sample_list=sample_list
        self.possibility_list=possibility_list
        self.all_combinations=self.fix_combinations(all_combinations)

    def fix_combinations(self, list_of_sets):
        return_list=[]
        for item in list_of_sets:
            item=list(item)
            return_list.append(str(item))
        return return_list

    def log_formula(self, x):
        return math.log2(1/x)

    def final_formula(self):
        bit_sum=[]
        possibility_sum=[]
        bit_dictionary={}
        
        word_combination=self.possibility_list[self.word]
        for combination in self.all_combinations:
            if combination in list(word_combination.keys()):
                # empty_sum.append(word_combination[combination]/5700)
                entropy=self.log_formula(word_combination[combination]/12897)
                bit_sum.append(entropy)
                possibility_sum.append((word_combination[combination]/12897)*entropy)

        return  sum(possibility_sum)



def main():
    N=5
    possible_values = [0,1,2]
    all_combinations = list(itertools.product(possible_values, repeat=N))

    empty_dictionary={}
    for word in sample_list:
        instantiated=CalculateBits(word, sample_list=sample_list, possibility_list=possibility_list, all_combinations=all_combinations)
        bits=instantiated.final_formula()
        empty_dictionary[word]=bits
        print(word, bits)

    # empty_dictionary=json.dumps(empty_dictionary)

    # f=open("total_bits.txt", "a")
    # f.write(empty_dictionary)
    # f.close()

   

if __name__ == "__main__":
    main()