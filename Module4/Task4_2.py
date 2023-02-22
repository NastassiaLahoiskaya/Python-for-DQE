import string
import random

# create a list of random number of dicts (from 2 to 10)
def create_list_of_dict(a=1, b=2, c=3, e=10, f=1):
    rand_list = []                                             # empty list
    for x in range(random.randint(a,b)):                      # generate random numbers of dictionaries
        size = c                                              # the size of dictionary
        keys = random.sample(string.ascii_lowercase,size)     # random letters in key parameters
        values = (random.randint(f,e) for y in range(size))   # random numbers in value parameters
        one_Dict = dict(zip(keys,values))                     # the dictionary can be created by pairing up the letters
        rand_list.append(one_Dict)                            # add it to the list
    return rand_list                                          # console output

dictList = create_list_of_dict(a=2, b=10, e=50)               # call the function with parameters
print('List of dictionaries: ', dictList)                     # console output

# get previously generated list of dicts and create one common dict
# create the function with 1 parameter for dictList
def create_lists_with_keys(lst):
    distinct_keys = []                         # create an empty list for distinct letters
    duplicated_keys = []                       # create an empty list for distinct letters which have duplicates

    for z in dictList:                         # go through each dictionary and each key
        for key in z:
            if key not in distinct_keys:       # if we have the specified key in 'distinct_keys' list-populate this list with each letter
                distinct_keys.append(key)      # populate this list with each letter only once
            elif key not in duplicated_keys:   # if we have duplicated key - populate "duplicated_keys"
                duplicated_keys.append(key)
    distinct_keys.sort()                        # sort "distinct_keys" list in alphabetical order
    duplicated_keys.sort()                      # sort "duplicated_keys" list in alphabetical order
    return distinct_keys, duplicated_keys

distinct_keys, duplicated_keys = create_lists_with_keys(dictList)  # call the function create_list_of_dict with parameter dictList

print('Distinct keys: ', distinct_keys)        # console output
print('Duplicated keys: ', duplicated_keys)    # console output

# create the function with 3 parameters for distinct_keys, duplicated_keys, list_of_dict
def create_one_common_dict(dist_k, dupl_k, lst):
    common_dict = {}                            # create an empty common dictionary
    for key in distinct_keys:                   # check if the letter is exists in 'duplicated_keys' list
        if key in duplicated_keys:
            max_value = 0                       # define max value for each key
            dict_number = 0                     # define the number of the dictionary in the list
            for i, rand_dict in enumerate(dictList):  # iterate over each dictionary and check if the specified key is in
                if key in rand_dict and rand_dict[key] > max_value:
                    max_value = rand_dict[key]  # update max value
                    dict_number = i + 1         # update the number of the dictionary
            key_final = key + '_' + str(dict_number)  # create the key and insert its max value into the common_dict
            common_dict.setdefault(key_final, max_value)
        if key not in duplicated_keys:          # check if the letter is NOT exists in 'duplicated_keys' list
            for rand_dict in dictList:          # iterate over each dictionary
                if key in rand_dict:            # check if the specified key is in the specified dictionary
                    common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the common_dict
    return common_dict

# call the function with 3 parameters
common_dict_final = create_one_common_dict(distinct_keys, duplicated_keys, dictList)
print('Common dictionary: ', common_dict_final)  # console output