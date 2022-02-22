import json
import itertools
import math


f=open("full_calculated_possibilities.txt")
test_string=f.read()
possibility_list = json.loads(test_string)

my_file = open("large_sample_size.txt", "r")

sample_list = my_file.read()
sample_list = sample_list.split(",")

class WordleFormula():
    def __init__(self, word=None, sample_list=sample_list, possibility_list=possibility_list, all_combinations=None):
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

    def cal_average(self, num):
        sum_num = 0
        for t in num:
            sum_num = sum_num + t           

        avg = sum_num / len(num)
        return avg

    def log_formula(self, x):
        return math.log(1/x,2)

    def final_formula(self):
        empty_sum=[]
        word_combination=self.possibility_list[self.word]
        for combination in self.all_combinations:
            if combination in list(word_combination.keys()):
                # empty_sum.append(word_combination[combination]/5700)
                entropy=self.log_formula(word_combination[combination]/5700)
                empty_sum.append(entropy)
        breakpoint()
        return self.cal_average(empty_sum)



def main():
    N=5
    possible_values = [0,1,2]
    all_combinations = list(itertools.product(possible_values, repeat=N))
    word='weary'
    instantiated=WordleFormula(word, sample_list=sample_list, possibility_list=possibility_list, all_combinations=all_combinations)

    word_entropy=instantiated.final_formula()

    print(word, word_entropy)
   

if __name__ == "__main__":
    main()