#%%
from wordle_oop import SolveWordle


my_file = open("large_sample_size.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split(",")
class WordleHelp(SolveWordle):

    def turn_1(self, results_after_guess):
        turn_1_results=self.type_outcome_faster(results_after_guess)
        print(turn_1_results[0])
        print(turn_1_results[1])
        print(turn_1_results[2])
        turn_1=self.refine_list(turn_1_results[0], turn_1_results[1], turn_1_results[2], sample_list )
        print(turn_1)
        self.make_guess(turn_1)
        return turn_1
    
    def turn_2(self, results_after_guess):
        turn_2_results=self.type_outcome_faster(results_after_guess)

        turn_2=self.refine_list(turn_2_results[0], turn_2_results[1], turn_2_results[2], self.turn_1)
        print(turn_2)
        self.make_guess(turn_2)

# %%
