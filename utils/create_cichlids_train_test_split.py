#make cichlids train and test list
import os
import numpy as np
import pandas as pd

train_list_file = '/Users/lijiang/Desktop/cichlids_train_list.txt'
test_list_file = '/Users/lijiang/Desktop/cichlids_test_list.txt'
dictionary_file = '/Users/lijiang/Desktop/classInd.txt'
jpg_folder = '/Users/lijiang/Desktop/jpgs'

def create_csv_file(split_ratio):
    with open(train_list_file,'w') as train_output, open(test_list_file,'w') as test_output:
    #loop through all the videos and give it to either train or test based on the split ratio
        categories = {}
        i = 0
        for folder in os.listdir(jpg_folder):
            folder_path = jpg_folder +'/' + folder
            if not os.path.isdir(folder_path):
                continue
            i += 1
            categories[folder] = i
            for file in os.listdir(folder_path):
                if not os.path.isdir(folder_path+'/'+file):
                    continue
                output_string = folder + '/' + file + ' '
                
                if np.random.uniform() < split_ratio:
                    output_string += str(i)+'\n'
                    train_output.write(output_string)
                
                else:
                    output_string += '\n'
                    test_output.write(output_string)
    with open(dictionary_file,'w') as output:
        for key,value in categories.items():
            output.write(str(value)+ ' '+ str(key)+'\n')
        


create_csv_file(0)