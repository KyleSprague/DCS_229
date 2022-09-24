import numpy as np

def readFile(filename: 'TextIO', use_dict: bool = False) -> "tuple[list] or dict": #3.10 or greater -> tuple[list] | dict: #3.9 or lower, use import typing or string
    '''
    Function to read a file and return information relating to the frequency of each word in the file

    Parameters:
        filename -- textIO: the .txt file that we are reading from
        use_dict -- boolean telling us whether to return a dictionary or not

    Returns a dictionary of word:frequency of occurence key values or a tuple containing a list of words and
    another constituent component of the tuple with their respective frequency

    '''

    file_object = open(filename)
    line = file_object.readline()
    text_list = []

    while line != "": #idea for while loop from my Netpbm.py ReadPGM pixels function from Fauxtoshop proj
        line_list = line.strip().split()
        text_list.append(line_list)
        #print(line_list)
        line = file_object.readline()

    word_list = []

    #contractions = {"'m": "am", "'ll": "will", "'d": "would"}
    # 'd can both mean had and would; who'd and you'd, for instance.
    # do I just treat contractions as one word?

    for element in text_list: #grabs a line
        for indx in range(len(element)): #indexes to word in line
            '''
                CHARACTERS THAT APPEAR AT THE END OF WORDS
            '''
            if element[indx].__contains__("?") or \
            element[indx].__contains__("!") or \
            element[indx].__contains__(".") or \
            element[indx].__contains__(":") or \
            element[indx].__contains__(";") or \
            element[indx].__contains__(","):
                #idea to use contains method comes from https://www.askpython.com/python/string/python-string-contains
                #print(f"word with punctuation is {element[index]}")
                element[indx] = element[indx].strip("?").strip("!").strip(".").strip(",").strip(":").strip(";")
            '''
                CHARACTERS THAT APPEAR IN THE MIDDLE OF WORDS OR AT THE BEGINNING OF WORDS
            '''

            '''
            if element[indx].__contains__('"'):
                istart = element[indx].index('"')
                iend = istart+1
                working_word = element[indx]
                replacement_1 = working_word[:istart] + working_word[iend:] #source:
                #https://github.com/astropgh/python-boot-camp-2022/tree/main/notebooks/01-PythonIntro
                #Data Structures Notebook Slicing section
                #print(replacement_1)
                element[indx] = replacement_1
            '''

            if element[indx].__contains__("\\"):
                istart = element[indx].index("\\")
                iend = istart+1
                working_word = element[indx]
                replacement_2 = working_word[:istart] + working_word[ined:]
                element[indx] = replacement_2

            if element[indx].__contains__("(") and element[indx].__contains__(")"):
                p1start = element[indx].index("(")
                p1end = p1start+1
                working_word = element[indx]
                replacement_3 = working_word[:p1start] + working_word[p1end:]

                p2start = replacement_3.index(")")
                p2end = p2start + 1
                replacement_4 = replacement_3[:p2start] + replacement_3[p2end:]
                element[indx] = replacement_4

            if element[indx].__contains__("-") and (element[indx][-1] == "-" or element[indx][-1] == "--"):
                replacement_5 = element[indx].strip("-")
                element[indx] = replacement_5
            elif element[indx].__contains__("-") and (element[indx][-1] != "-" or element[indx][-1] != "--"):
                working_word = element[indx]
                hyphen_start_loc = working_word.index("-")
                word_1 = working_word[:hyphen_start_loc]
                word_2 = working_word[hyphen_start_loc+1:]
                element[indx] = (word_1, word_2)

            if isinstance(element[indx], tuple) == False:
                current_word = element[indx].lower()
                word_list.append(current_word)
            else:
                word_list.append(element[indx])

    #print(word_list)

    tuple_list = [j for j in word_list if isinstance(j, tuple) == True]
    #list of tuples in song, which come from hyphenated words

    if tuple_list:
        #print(tuple_list)
        for i in range(len(tuple_list)):
            tuple_word_1, tuple_word_2 = tuple_list[i]
            #print(tuple_word_1)
        #for i in range(len(word_list)):
            #if isinstance(word_list[i], tuple) == True:
            word_list.append(tuple_word_1)
            word_list.append(tuple_word_2)

        word_list_revised = []
        tuple_index_list = [word_list.index(k) for k in word_list if isinstance(k, tuple) == True]
        for w in range(len(tuple_index_list)):
            removal_value = tuple_index_list[w] #value at w is index of tuple in word list
            #print(removal_value)
            for x in range(len(word_list)):
                if word_list[x] != word_list[removal_value]:
                    word_list_revised.append(word_list[x].lower())
        word_list = word_list_revised.copy()

    print(f"the number of words in the word_list is {len(word_list)}")

    #print(word_list)

    #ALT unique_word_set = set(word_list) #does unique mean the word does not appear twice?
    unique_word_list = list(np.unique(np.array(word_list))) #is using numpy okay?
    # ALT unique_word_list = list(unique_word_set)
    # ALT print(unique_word_list)
    if use_dict == False:

        i = 0
        count_list = []
        #print(len(word_list))

        #ALT
        #while i < len(word_list):
            #count = word_list.count(unique_word_list[i])
            #count_list.append(count)
            #i+=1

        while i < (len(unique_word_list)):
            count = word_list.count(unique_word_list[i])
            count_list.append(count)
            i+=1
            #print(sum(count_list))
            #print(len(count_list))
            #print(count_list)

        file_object.close()
        print(f"total_words in unique_word_list is {sum(count_list)}")
        return unique_word_list, count_list

    if use_dict != False:
        count_list = []
        i = 0
        while i < (len(unique_word_list)):
            count = word_list.count(unique_word_list[i])
            count_list.append(count)
            i+=1

        print(f"total_words in unique_word_list is {sum(count_list)}")
        my_dict = {}
        for j in range(len(unique_word_list)):
            key = unique_word_list[j]
            #print(key)
            value = (count_list[j])
            my_dict.update({key:value})

        #for i in range((len(composite_list)))
        #print(unique_word_list)

        return my_dict

def writeTopTen(input_dictionary: dict, testing_file: 'TextIO') -> None: #assume at least 10 unique words
    '''
        Function that writes to a file a list of words and their respective frequency in
        descending order of frequency

        Parameters:
            input_dictionary -- dict: dictionary containing word:frequency of word key value pairs
            testing_file -- textIO: an text file that will be written over

        Returns:
            None; function is nonfruitful
    '''
    file_handle = open(testing_file, "w")

    sorted_dictionary = {k: v for k, v in sorted(input_dictionary.items(), key=lambda item: item[1], reverse = True)} #from StackOverflow on class Friday
    #print(sorted_dictionary)

    count = 0
    dict_list = list(sorted_dictionary.values())
    #print(f"dict list is {dict_list}")
    new_dict = {}
    old_value = dict_list[0]
    for k,v in sorted_dictionary.items():
        if count < 10:
            count +=1
            old_value = v
            #print(type(v))
            file_handle.write(f"{k} {v}" + "\n")
        elif count >= 10 and v == old_value:
            file_handle.write(f"{k} {v}" + "\n")
            count+=1

    file_handle.close()
    #PRECLASS values_list = list(input_dictionary.values())
    #PRECLASS sorted_values = []
    #PRECLASS for i in range(len(values_list)):
    #PRECLASS    sorted_values.append(int(values_list[i]))
    #PRECLASS sorted_values.sort(reverse = True) #this is a list of word numbers in descending order


    #PRECLASS short_list = []
    #PRECLASS initial_value = sorted_values[0]
    #PRECLASS for j in range(len(sorted_values)):
    #PRECLASS     return None #I need help with this for loop

    #to find top 2
    #{k: v for k, v in sorted(x.items(), key=lambda item: itme[1])}
    # lambda says def key(item): return item[1]
    # x.items() gives us items in the dictionary as key,value pairs
    # sorted gives back a sorted list according to second value in tuple (aka the value)



    #print(short_list)

    #print(sorted_values)

def main():

    print("--------------WILCO TESTING------------------")
    file_name = "wilco.txt"
    result = readFile(file_name)
    print("----------------------------------------------------")
    print(f"Result for Wilco file is {result}")
    wilco_dict_result = readFile("wilco.txt", use_dict = True )
    print(f"Result for Wilco with dictionary is {wilco_dict_result}")
    print("---------------------------------------------------")
    new_file = "wilco_writing_file"
    writeTopTen(wilco_dict_result, new_file)

    ############################## MY TESTING ####################################

    print("-------------------------MY TESTING------------------------")
    file_1 = open("file_1.txt", "w")
    file_1.write('"I\'m twisted (twisted) \n I\'ll contradict it, keep him addicted \n Lies on his lips, I lick it \n \n Unique" ')
    #BEYONCE: "Alien Superstar"
    file_1.close()
    t1_result = readFile("file_1.txt")
    print(f"result for test_1 without dictionary is {t1_result}")
    print("-----------------------------------------------------")
    t1_result_dict = readFile("file_1.txt", use_dict = True)
    print(f"result for test_1 with dictionary is {t1_result_dict}")
    print("-----------------------------------------------------")
    beyonce_file = "Beyonce_writing_file"
    writeTopTen(t1_result_dict, beyonce_file)
    print("-----------------------------------------------------")

    print("####################SECOND FILE#######################")
    file_2 = open("file_2.txt", "w")
    file_2.write('Summertime, city life, Chi-town, my town, my town \n\
    After school matters like I\'m needing that stipend right now \n\
    Kennicott parking lot got caught with the blunt like "wow wow"')
    #Noname: "Diddy Bop"
    file_2.close()
    t2_result = readFile("file_2.txt")
    print(f"result for test_2 without dictionary is {t2_result}")
    print("-----------------------------------------------------")
    t2_result_dict = readFile("file_2.txt", use_dict = True)
    print(f"result for test_2 with dictionary is {t2_result_dict}")
    print("-----------------------------------------------------")
    noname_file = "Noname_writing_file"
    writeTopTen(t2_result_dict, noname_file)


if __name__ == "__main__":
  main()



#HEELLLOOOOOOOO




#NOTE: TRY TO ACCOUNT FOR CONTRACTIONS UPON RETURN!!!!!!!
