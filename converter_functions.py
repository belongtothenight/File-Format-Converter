import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob
import tkinter as tk
from tkinter import filedialog
import subprocess as sp
import numpy as np
import pathlib as pl
import csv

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
            folder_path: (str) path of folder.
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
            file_path: (str) path of file.
    Link:
        https://www.codegrepper.com/code-examples/python/Python+open+file+explorer+to+select+file
    '''
    #print('\n\nExecuting select_file function')
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename()
    print("converter_function.py-> Selected file path: ", file_path)
    return file_path

def user_input():
    '''
    Description:
        This function selects a file.
    parameter:
        Input:
            None
        Output:
            (str) user input.
    Link:
        https://www.mikedane.com/programming-languages/python/getting-user-input/
    '''
    return input('Please enter your input: ')

#def md_to_csv():

def csv_to_md(file, folder, md_name, md_title, md_frame):
    '''
    Description:
        This function converts csv files to md files in the same folder.
    parameter:
        Input:
            file: (str) path of csv file and its file name. Ex: "D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1/file_list.csv"
            folder: (str) path of csv file. Ex: "D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1/"
            md_name: (str) name of md file. Ex: "file_list_basic"
            md_title: (str) title of md file. Ex: "Image"
            md_frame: (str) frame of md file. Ex: "Test Frame"
        Output:
            None
    Link:
        https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
        https://www.pythontutorial.net/python-basics/python-write-text-file/
        https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html
    '''
    file_path = file
    folder_path = folder
    title = md_title
    frame = md_frame
    name = md_name
    data = pd.read_csv(file_path, encoding= 'utf-8')
    #print(data)
    df = pd.DataFrame(data)
    md_basic = df.to_markdown()
    md_tabulate = df.to_markdown(tablefmt='grid')
    #print(md_basic)
    #print(md_tabulate)

    #'''Export basic markdown file
    with open(folder_path + name + ".md", 'w') as f:
        f.write("# " + title + "\n")
        f.write("[[" + frame + "]]" + "\n\n")
        f.write(md_basic)
        f.close()
    print(folder_path + name + ".md")
    print('Execute successful, md file exported')
    #'''

    '''Export tabulate markdown file (doesn't look good as markdown, better as txt)
    with open(folder_path + name + ".md", 'w') as f:
        f.write("# " + title + "\n")
        f.write("[[" + frame + "]]" + "\n\n")
        f.write(md_tabulate)
        f.close()
    print(folder_path + name + ".md")
    print('Execute successful, md file exported')
    '''

def xml_to_csv(xml_file_path, csv_file_path_name):
    '''
    Description:
        This function converts xml files exported from labelimg to csv files.
    parameter:
        Input:
            xml_file_path: (str) path of xml files. Ex: 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/xml'
            csv_file_path_name: (str) path of csv files and its file name. Ex: 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/train2.csv'
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

def bulk_file_rename_csv(source_folder_path, source_file_type, generate_file_name, generate_filename_counter_init):
    '''
    Description:
        This function create a new xlsx file in the target directory and provide user commands to copy and paste in command prompt in order to rename large amount of files as numbers at the same time.
    parameter:
        Input:
            source_folder_path: (str) path of source folder, which is where those needed to be renamed are stored at. Ex: 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1/'
            source_file_type: (str) file type of source files, only include a single file type per run. Ex: ".jpg"
            generate_file_name: (str) file name of generate file, which is the xlsx file's name that will be created. Ex: 'file_list.xlsx'
            generate_filename_counter_init: (int) initial value of generated filename counter. Ex: 1, 1001, or 2001
        Output:
            None
    Link:
        https://stackoverflow.com/questions/21406887/subprocess-changing-directory
        https://www.geeksforgeeks.org/python-string-split/
        https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
        https://stackoverflow.com/questions/11106536/adding-row-column-headers-to-numpy-arrays
        https://www.codegrepper.com/code-examples/python/fill+empty+rows+with+nan+pandas
        https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu
        https://stackoverflow.com/questions/43561622/merge-two-numpy-arrays
        https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values
        https://blog.csdn.net/BBJG_001/article/details/104165479
        https://blog.csdn.net/qq_43893755/article/details/115225419
        https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html
        https://stackoverflow.com/questions/42330201/assign-values-to-array-during-loop-python
        https://appdividend.com/2022/06/15/how-to-convert-python-tuple-to-array/
        https://stackoverflow.com/questions/35940748/use-python-to-launch-excel-file
        https://www.codegrepper.com/code-examples/python/python+open+excel+file
        https://stackoverflow.com/questions/281888/open-explorer-on-a-file
        https://stackoverflow.com/questions/4119166/replace-backslashes-with-forward-slashes-in-python
    '''
    folder_path = source_folder_path
    file_type = source_file_type
    file_name = generate_file_name
    csv_col_3_init = generate_filename_counter_init #New file name starts from 1
    csv_col_4_init = "ren" #CMD rename command
    csv_col_5_init = 2 #Full command formula counter starts from 2
    #csv_col_5_init = "=D2&\" \"\"\"&A2&\"\"\" \"\"\"&C2&B2&\"\"\"\"" #Full command
    csv_col_5_init_1 = "=D"
    csv_col_5_init_2 = "&\" \"\"\"&A"
    csv_col_5_init_3 = "&\"\"\" \"\"\"&C"
    csv_col_5_init_4 = "&B"
    csv_col_5_init_5 = "\"\"\"\""
    file_count_init = 0
    null_counter = 0
    filtered_file_list = []
    csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command', 'Full Command']]
    #csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command']]

    #print(csv_col_5_init)
    #print(csv_col_5_init_1+csv_col_5_init_2+csv_col_5_init_3+csv_col_5_init_4+csv_col_5_init_5)

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

    np_col_3 = [str(csv_col_3_init + null_counter) for null_counter in range(0,file_count_init)]
    np_col_3 = np.asarray(np_col_3)
    np_col_3 = np_col_3[np.newaxis,:]
    #for element in np_col_3: print(element)

    np_col_4 = np.full((1, file_count_init), csv_col_4_init)
    #for element in np_col_4: print(element)

    np_col_5 = [csv_col_5_init_1 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_2 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_3 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_4 + (str(csv_col_5_init + null_counter)) for null_counter in range(0,file_count_init)]
    np_col_5 = np.asarray(np_col_5)
    np_col_5 = np_col_5[np.newaxis,:]
    #for element in np_col_5: print(element)

    np_col = np.concatenate((np_col_1, np_col_2, np_col_3, np_col_4, np_col_5), axis=0)
    #for element in np_col: print(element)
    np_col = np.swapaxes(np_col, 0, 1)
    #for element in np_col: print(element)

    df = pd.DataFrame(np_col, columns=csv_col)
    df.to_csv(folder_path + file_name, index=False)
    print('Execute successful, csv file exported')

    p = pl.PureWindowsPath(rf'{folder_path}{file_name}')
    print(str(p))

    # Launch excel file (doesn't work)
    #os.system(f'start excel "{str(p)}"')

    # Launch file explorer
    sp.Popen(f'explorer /select, "{str(p)}"')
    print('Execute successful, csv file opened')

def bulk_file_rename_xlsx(source_folder_path, source_file_type, generate_file_name, generate_filename_counter_init):
    '''
    Description:
        This function create a new xlsx file in the target directory and provide user commands to copy and paste in command prompt in order to rename large amount of files as numbers at the same time.
    parameter:
        Input:
            source_folder_path: (str) path of source folder, which is where those needed to be renamed are stored at. Ex: 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1/'
            source_file_type: (str) file type of source files, only include a single file type per run. Ex: ".jpg"
            generate_file_name: (str) file name of generate file, which is the xlsx file's name that will be created. Ex: 'file_list.xlsx'
            generate_filename_counter_init: (int) initial value of generated filename counter. Ex: 1, 1001, or 2001
        Output:
            None
    Link:
        https://stackoverflow.com/questions/21406887/subprocess-changing-directory
        https://www.geeksforgeeks.org/python-string-split/
        https://www.freecodecamp.org/news/python-strip-how-to-trim-a-string-or-line/
        https://stackoverflow.com/questions/11106536/adding-row-column-headers-to-numpy-arrays
        https://www.codegrepper.com/code-examples/python/fill+empty+rows+with+nan+pandas
        https://stackoverflow.com/questions/34509198/no-module-named-openpyxl-python-3-4-ubuntu
        https://stackoverflow.com/questions/43561622/merge-two-numpy-arrays
        https://stackoverflow.com/questions/5891410/numpy-array-initialization-fill-with-identical-values
        https://blog.csdn.net/BBJG_001/article/details/104165479
        https://blog.csdn.net/qq_43893755/article/details/115225419
        https://numpy.org/doc/stable/reference/generated/numpy.swapaxes.html
        https://stackoverflow.com/questions/42330201/assign-values-to-array-during-loop-python
        https://appdividend.com/2022/06/15/how-to-convert-python-tuple-to-array/
        https://stackoverflow.com/questions/35940748/use-python-to-launch-excel-file
        https://www.codegrepper.com/code-examples/python/python+open+excel+file
        https://stackoverflow.com/questions/281888/open-explorer-on-a-file
        https://stackoverflow.com/questions/4119166/replace-backslashes-with-forward-slashes-in-python
    '''
    folder_path = source_folder_path
    file_type = source_file_type
    file_name = generate_file_name
    csv_col_3_init = generate_filename_counter_init #New file name starts from 1
    csv_col_4_init = "ren" #CMD rename command
    csv_col_5_init = 2 #Full command formula counter starts from 2
    #csv_col_5_init = "=D2&\" \"\"\"&A2&\"\"\" \"\"\"&C2&B2&\"\"\"\"" #Full command
    csv_col_5_init_1 = "=D"
    csv_col_5_init_2 = "&\" \"\"\"&A"
    csv_col_5_init_3 = "&\"\"\" \"\"\"&C"
    csv_col_5_init_4 = "&B"
    csv_col_5_init_5 = "\"\"\"\""
    file_count_init = 0
    null_counter = 0
    filtered_file_list = []
    csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command', 'Full Command']]
    #csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command']]

    #print(csv_col_5_init)
    #print(csv_col_5_init_1+csv_col_5_init_2+csv_col_5_init_3+csv_col_5_init_4+csv_col_5_init_5)

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

    np_col_3 = [str(csv_col_3_init + null_counter) for null_counter in range(0,file_count_init)]
    np_col_3 = np.asarray(np_col_3)
    np_col_3 = np_col_3[np.newaxis,:]
    #for element in np_col_3: print(element)

    np_col_4 = np.full((1, file_count_init), csv_col_4_init)
    #for element in np_col_4: print(element)

    np_col_5 = [csv_col_5_init_1 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_2 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_3 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_4 + (str(csv_col_5_init + null_counter)) for null_counter in range(0,file_count_init)]
    np_col_5 = np.asarray(np_col_5)
    np_col_5 = np_col_5[np.newaxis,:]
    #for element in np_col_5: print(element)

    np_col = np.concatenate((np_col_1, np_col_2, np_col_3, np_col_4, np_col_5), axis=0)
    #for element in np_col: print(element)
    np_col = np.swapaxes(np_col, 0, 1)
    #for element in np_col: print(element)

    df = pd.DataFrame(np_col, columns=csv_col)
    df.to_excel(folder_path + file_name, index=False)
    print('Execute successful, xlsx file exported')

    p = pl.PureWindowsPath(rf'{folder_path}{file_name}')
    print(str(p))

    # Launch excel file (doesn't work)
    #os.system(f'start excel "{str(p)}"')

    # Launch file explorer
    sp.Popen(f'explorer /select, "{str(p)}"')
    print('Execute successful, xlsx file opened')





