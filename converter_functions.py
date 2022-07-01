import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob
import tkinter as tk
from tkinter import filedialog
import subprocess as sp
import numpy as np

os.system('cls')
print('This is a library file, not a main file.\n\n')

def select_folder_path():
    '''
    Description:
        This function selects a folder path.
    parameter:
        Input:
            None
        Output:
            folder_path: path of folder.
    Link:
        https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python
    '''
    #print('\n\nExecuting select_folder_path function')
    tk.Tk().withdraw()
    folder_path = filedialog.askdirectory()
    print("converter_function.py-> Selected folder path: ", folder_path)
    return folder_path

def select_file():
    '''
    Description:
        This function selects a file.
    parameter:
        Input:
            None
        Output:
            file_path: path of file.
    Link:
        https://www.codegrepper.com/code-examples/python/Python+open+file+explorer+to+select+file
    '''
    #print('\n\nExecuting select_file function')
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename()
    print("converter_function.py-> Selected file path: ", file_path)
    return file_path

# def user_input():

def xml_to_csv(xml_file_path, csv_file_path_name):
    '''
    Description:
        This function converts xml files exported from labelimg to csv files.
    parameter:
        Input:
            xml_file_path: path of xml files.
            csv_file_path_name: path of csv files and its file name.
        Output:
            None
    Link:
        https://github.com/belongtothenight/FRCNN_Related_Code/blob/main/Format%20Converter%20xml%20to%20csv%20V2.py
    '''
    print('\n\nExecuting xml_to_csv function')
    xml_list = []
    for xml_file in glob.glob(xml_file_path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(os.path.splitext(root.find('filename').text)[0]),#Image file name needs to be purely with numbers!! No space is allowed.
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename',  'PicIndex', 'type', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    xml_df_sort = xml_df.sort_values(by=['PicIndex'])
    xml_df_sort_less = xml_df_sort.drop("PicIndex", axis=1)
    xml_df_sort_less.to_csv(csv_file_path_name, index=False)
    print(xml_df_sort_less, '\n\nexecute successful, csv file exported')

#def bulk_file_rename():

folder_path = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1'
file_type = ".jpg"
file_count_init = 0
null_counter = 0
filtered_file_list = []
#csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command', 'Full Command']]
csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name']]
csv_col_3_init = 1

# Read xml file and store in a array
output = sp.run('dir /b /o:n', cwd=folder_path, shell=True, stdout=sp.PIPE)
output_str = str(output.stdout)
stripped_output_str = output_str.strip("b'")
split_stripped_output_str = stripped_output_str.split('\\r\\n')
for line in split_stripped_output_str:
    if file_type in line:
        filtered_file_list.append(line)
        file_count_init += 1
        #print(line)
#print(file_count_init)
#np.savetxt(folder_path + '/file_list.csv', filtered_file_list, delimiter=',', fmt='%s')
np_col_1 = np.array(filtered_file_list)
np_col_1 = np_col_1[np.newaxis,:]
#for element in np_col_1: print(element)

np_col_2 = np.full((1, file_count_init), file_type)
#for element in np_col_2: print(element)

np_col_3 = [(csv_col_3_init + null_counter) for null_counter in range(0,file_count_init)]
np_col_3 = np.asarray(np_col_3)
np_col_3 = np_col_3[np.newaxis,:]
#for element in np_col_3: print(element)

np_col = np.concatenate((np_col_1, np_col_2, np_col_3), axis=0)
for element in np_col: print(element)
np_col = np.swapaxes(np_col, 0, 1)
for element in np_col: print(element)

df = pd.DataFrame(np_col, columns=csv_col)
df.to_excel(folder_path + '/file_list.xlsx', index=False)
print('Execute successful, xlsx file exported')

# https://stackoverflow.com/questions/21406887/subprocess-changing-directory
# https://www.geeksforgeeks.org/python-string-split/
# https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
# https://stackoverflow.com/questions/11106536/adding-row-column-headers-to-numpy-arrays
# https://www.codegrepper.com/code-examples/python/fill+empty+rows+with+nan+pandas
# https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu
# https://stackoverflow.com/questions/43561622/merge-two-numpy-arrays
# https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values
# https://blog.csdn.net/BBJG_001/article/details/104165479
# https://blog.csdn.net/qq_43893755/article/details/115225419
# https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html
# https://stackoverflow.com/questions/42330201/assign-values-to-array-during-loop-python
