import random
import string

# create a list of random number of dicts (from 2 to 10)

rand_list = []  # empty list
for j in range(random.randint(2, 10)):  # generate random numbers of dictionaries
    size = 3  # the size of dictionary
    keys = random.sample(string.ascii_lowercase, size)  # random letters in key parameters
    values = (random.randint(0, 100) for y in
              range(size))  # random numbers in value parameters and random letters in key parameters
    one_Dict = dict(zip(keys, values))  # the dictionary for connecting letters
    rand_list.append(one_Dict)  # add them into the list

print(rand_list)  # console output

# get previously generated list of dicts and create one common dict

distinct_keys = []  # create an empty list for distinct letters
duplicated_keys = []  # create an empty list for distinct letters which have duplicates

for z in rand_list:  # go through each dictionary and each key
    for key in z:
        if key not in distinct_keys:  # if we have the specified key in 'distinct_keys' list-populate this list with each letter
            distinct_keys.append(key)
        elif key not in duplicated_keys:  # if we have duplicated key - populate "duplicated_keys"
            duplicated_keys.append(key)

distinct_keys.sort()  # sorting 'distinct_keys' list in alphabetical order
duplicated_keys.sort()  # sorting 'duplicated_keys' list in alphabetical order
print('Distinct keys: ', distinct_keys)  # console output
print('Duplicated keys: ', duplicated_keys)  # console output

common_dict = {}  # create an empty common dictionary

for key in distinct_keys:
    if key in duplicated_keys:  # check if the letter is exists in 'duplicated_keys' list
        max_value = 0  # define max value for each key
        dict_number = 0  # define the number of the dictionary in the list
        for i, rand_dict in enumerate(rand_list):  # iterate over each dictionary and check if the specified key is in
            if key in rand_dict and rand_dict[key] > max_value:
                max_value = rand_dict[key]  # update max value
                dict_number = i + 1  # update the number of the dictionary
        key_final = key + '_' + str(dict_number)  # create the key and insert its max value into the common_dict
        common_dict.setdefault(key_final, max_value)
    if key not in duplicated_keys:  # check if the letter is NOT exists in 'duplicated_keys' list
        for rand_dict in rand_list:  # iterate over each dictionary
            if key in rand_dict:  # check if the specified key is in the specified dictionary
                common_dict.setdefault(key, rand_dict[key])  # insert key and its value in the common_dict

print('Common dictionary: ', common_dict)  # console output
