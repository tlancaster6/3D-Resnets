#make cichlids train and test list
import os
import numpy as np
spit_folder = '/Users/lijiang/Desktop/new_split_with_focus/video/spit'
scoop_folder = '/Users/lijiang/Desktop/new_split_with_focus/video/scoop'
train_list_file = '/Users/lijiang/Desktop/cichlids_train_list.txt'
test_list_file = '/Users/lijiang/Desktop/cichlids_test_list.txt'

def create_csv_file(split_ratio):
    with open(train_list_file,'w') as train_output, open(test_list_file,'w') as test_output:
    #loop through all the videos and give it to either train or test based on the split ratio
        for file in os.listdir(spit_folder):
            if not file.startswith('MC'):
                continue
            output_string = 'spit/'
            output_string += file
            
            if np.random.uniform() < split_ratio:
                output_string += ' 1\n'
                train_output.write(output_string)
            else:
                output_string += '\n'
                test_output.write(output_string)
        for file in os.listdir(scoop_folder):
            if not file.startswith('MC'):
                continue
            output_string = 'scoop/'
            output_string += file
            if np.random.uniform() < split_ratio:
                output_string += ' 2\n'
                train_output.write(output_string)
            else:
                output_string += '\n'
                test_output.write(output_string)

create_csv_file(0.9)