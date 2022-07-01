import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob
import tkinter as tk
from tkinter import filedialog

print('This is a library file, not a main file.')

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

def bulk_file_rename():
    '''
    Description:
        This function renames all files in a folder.
    parameter:
        Input:
            file_path: path of files.
            file_name_prefix: prefix of file name.
            file_name_suffix: suffix of file name.
        Output:
            None
    Link:
        None
    '''
    print('\n\nExecuting bulk_file_rename function')
    
    '''
    for file_name in os.listdir(file_path):
        os.rename(os.path.join(file_path, file_name), os.path.join(file_path, file_name_prefix + file_name_suffix))
    '''

    print('\n\nExecute successful, all files renamed')

print('dir')
os.system('dir')



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