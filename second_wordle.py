#%%
my_file = open("large_sample_size.txt", "r")
sample_list = my_file.read()
sample_list = sample_list.split("")

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
def common_elements(test_list):
        res = []
        for i in test_list:
            if i not in res:
                res.append(i)
        res.sort()
        return res

def elimante_most_words(sample_list):
    dict_of_letters=find_best_letter(sample_list)
    list_of_letters_in_order=list(dict_of_letters)
    print(list_of_letters_in_order)
    list_to_add_to=[]
    for word in sample_list:
        
        if list_of_letters_in_order[0] not in word and list_of_letters_in_order[1] not in word and list_of_letters_in_order[2] not in word and list_of_letters_in_order[3] not in word and list_of_letters_in_order[6] not in word:
                list_to_add_to.append(word)
    print(len(list_to_add_to))
    remove_duplicates=common_elements(list_to_add_to)  
    print(len(remove_duplicates))      
elimante_most_words(sample_list)
            
# %%
