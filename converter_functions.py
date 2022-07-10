import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import os
import glob
import tkinter as tk
from tkinter import filedialog
import subprocess as sp
from pathlib import Path

os.system('cls')
#print('This is a library file, not a main file.\n\n')

#===============================================================================================================
# Sub-function

def select_folder_path():
    '''
    Description:
        This function selects a folder path.
    parameter:
        Parameter:
            None
        Return:
            folder_path: (str) path of folder.
        Output:
            None
    Sample Code:
        import converter_functions as cf
        cf.select_folder_path()
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
        Parameter:
            None
        Return:
            file_path: (str) path of file.
        Output:
            None
    Sample Code:
        import converter_functions as cf
        cf.select_file()
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
        Parameter:
            None
        Return:
            user_input: (str) user input.
        Output:
            None
    Sample Code:
        import converter_functions as cf
        print(cf.user_input())
    Link:
        https://www.mikedane.com/programming-languages/python/getting-user-input/
    '''
    return input('Please enter your input: ')

#list files in a folder (including subfolder)

#===============================================================================================================
# Main function

def md_to_csv(fp1, fp2, mdfn, csvfn):
    '''
    Description:
        This function converts md files to csv files in the same folder. It can only convert the first table in markdown file correctly.
    parameter:
        Parameter:
            fp1: (str) path of source folder.
            fp2: (str) path of export folder.
            mdfn: (str) file name of markdown file.
            csvfn: (str) file name of csv file.
        Return:
            None
        Output:
            csv file: Contains only the converted data.
    Sample Code:
        import converter_functions as cf
        fp1 = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file"
        fp2 = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file"
        mdfn = "file_list_basic.md"
        csvfn = "file_list_basic.csv"
        cf.md_to_csv(fp, mdfn, csvfn)
    Link:
        https://github.com/tomroy/mdtable2csv/blob/master/mdtable2csv
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    '''
    # dtype not used in this function
    sourcefolderpath = fp1
    exportfolderpath = fp2
    md_filename = mdfn
    csv_filename = csvfn

    path_a = sourcefolderpath + "/" + md_filename
    path_b = exportfolderpath + "/" + csv_filename
    line_counter = 0
    data = []
    # open markdown file
    with open (path_a, 'r') as f:
        md = f.read()
    split_md = md.splitlines()
    for line in split_md:
        if line.startswith("|"):
            line_counter += 1
            if (line_counter) == 1:
                category = line.split("|")
                category_counter = len(category) - 2 # there are one extra column at the start and end of the table
                del category[0]
                del category[-1]
                for i in range(0, category_counter): 
                    category[i] = category[i].strip()
                    #print(category[i])
            elif (line_counter) == 2:
                continue
            else:
                buffer = line.split("|")
                del buffer[0]
                del buffer[-1]
                for i in range(0, category_counter):
                    buffer[i] = buffer[i].strip()
                    #print(buffer[i])
                data.append(buffer)
    # Data inspection
    #print(category_counter)
    #print(category)
    #print(data)

    table = pd.DataFrame(data, columns=category)
    table.to_csv(path_b, index=False)
    print("Execute successful, csv file exported\n")

def csv_to_md(fp1, fp2, csvfn, mdfn, md_title, md_frame):
    '''
    Description:
        This function converts csv files to md files in the same folder.
    parameter:
        Parameter:
            file: (str) path of csv file and its file name.
            folder: (str) path of csv file.
            md_name: (str) name of md file.
            md_title: (str) title of md file.
            md_frame: (str) frame of md file.
        Return:
            None
        Output:
            Markdown file: Consisted with a title, page frame, and data table.
    Sample Code:
        import converter_functions as cf
        file_path = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/file_list.csv"
        folder_path = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/"
        name = "file_list_basic"
        title = "Image"
        frame = "Test Frame"
        cf.csv_to_md(file_path, folder_path, name, title, frame)
    Link:
        https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
        https://www.pythontutorial.net/python-basics/python-write-text-file/
        https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s
        https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html
    '''
    #file_path = fp1 + "/" + csvfn
    #folder_path = fp2
    #title = md_title
    #frame = md_frame
    #name = mdfn
    filepath_a = fp1 + "/" + csvfn
    filepath_b = fp2 + "/" + mdfn

    data = pd.read_csv(filepath_a, encoding= 'utf-8')
    #print(data)
    df = pd.DataFrame(data)
    md_basic = df.to_markdown()

    #Export basic markdown file
    with open(filepath_b, 'w') as f:
        #f.write("# " + md_title + "\n")
        #f.write("[[" + md_frame + "]]" + "\n\n")
        f.write(md_basic)
        f.close()
    print('Execute successful, md file exported')

def xml_to_csv(xml_file_path, csv_file_path_name):
    '''
    Description:
        This function converts xml files exported from labelimg to csv files.
    parameter:
        Parameter:
            xml_file_path: (str) path of xml files.
            csv_file_path_name: (str) path of csv files and its file name.
        Return:
            None
        Output:
            CSV file: Contains only the converted data.(without column name)
    Sample Code:
        import converter_functions as cf
        path1 = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/xml"
        path2 = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/train2.csv"
        cf.xml_to_csv(path1, path2)
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

def bulk_file_rename(source_folder_path, source_file_type, renamed_filename_counter_init, generate_file):
    '''
    Description:
        This function renames large amount of specific type of files in a folder, and can export csv or xlsx file with cmd renaming command.
    parameter:
        Parameter:
            source_folder_path: (str) path of source folder, which is where those needed to be renamed are stored at.
            source_file_type: (str) file type of source files, only include a single file type per run.
            renamed_filename_counter_init: (int) initial value of generated filename counter.
            generate_file: (str) None, CSV, or EXCEL, decide whether to generate csv or xlsx file.
        Return:
            None
        Output:
            None
            CSV file: Contains the list of filename.
            EXCEL file: Contains the list of filename.
    Sample Code:
        import converter_functions as cf
        folder_path = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/jpg/"
        file_type = ".jpg"
        csv_col_3_init = 1001 # New file name starts from 1
        file_generation = "None" # None, EXCEL or CSV
        cf.bulk_file_rename(folder_path, file_type, csv_col_3_init, file_generation)
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
        https://numpy.org/doc/stable/reference/generated/numpy.squeeze.html
    '''
    folder_path = source_folder_path
    file_type = source_file_type
    csv_col_3_init = renamed_filename_counter_init #New file name starts from 1
    csv_col_4_init = "ren" #CMD rename command
    csv_col_5_init = 2 #Full command formula counter starts from 2
    #csv_col_5_init = "=D2&\" \"\"\"&A2&\"\"\" \"\"\"&C2&B2&\"\"\"\"" #Full command
    csv_col_5_init_1 = "=D"
    csv_col_5_init_2 = "&\" \"\"\"&A"
    csv_col_5_init_3 = "&\"\"\" \"\"\"&C"
    csv_col_5_init_4 = "&B"
    csv_col_5_init_5 = "&\"\"\"\""
    file_count_init = 0
    null_counter = 0
    status = False
    filtered_file_list = []
    csv_col = [_ for _ in ['Old file name', 'Extension', 'New file name', 'Command', 'Full Command']]

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

    if generate_file == "None":
        pass
    elif generate_file == "CSV":
        np_col_1 = np.swapaxes(np_col_1, 0, 1)
        np_col_2 = np.swapaxes(np_col_2, 0, 1)
        np_col_3 = np.swapaxes(np_col_3, 0, 1)
        np_col_4 = np.swapaxes(np_col_4, 0, 1)
        np_col_5 = ["command buffer ==========================="]*file_count_init # if the output command isn't complete, add more characters in the brackets
        np_col_5 = np.array(np_col_5)
        for i in range(0, file_count_init):
            np_col_5[i] = str(np_col_4[i][0]) + " \"" + str(np_col_1[i][0]) + "\" \"" + str(np_col_3[i][0]) + str(np_col_2[i][0]) + "\""
        np_col_5 = np_col_5[np.newaxis,:]
        np_col_5 = np.swapaxes(np_col_5, 0, 1)
        np_col_1 = np.swapaxes(np_col_1, 0, 1)
        np_col_2 = np.swapaxes(np_col_2, 0, 1)
        np_col_3 = np.swapaxes(np_col_3, 0, 1)
        np_col_4 = np.swapaxes(np_col_4, 0, 1)
        np_col_5 = np.swapaxes(np_col_5, 0, 1)
        np_col = np.concatenate((np_col_1, np_col_2, np_col_3, np_col_4, np_col_5), axis=0)
        np_col = np.swapaxes(np_col, 0, 1)

        # Relocate directory
        p = Path(folder_path)
        p = p.parent.absolute()
        p = str(p) + "\\" + "file_list.csv"
        print(p)

        # Write to csv file
        df = pd.DataFrame(np_col, columns=csv_col)
        try:
            df.to_csv(p, index=False)
        except PermissionError:
            print("Permission denied, please close the file and try again.")
            status = True
            pass
        if status == False: print('Execute successful, csv file exported\n')

        # Launch file explorer
        '''
        sp.Popen(f'explorer /select, "{str(p)}"')
        print('Execute successful, csv file opened')
        '''
    elif generate_file == "EXCEL":
        # Command for excel file
        np_col_5 = [csv_col_5_init_1 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_2 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_3 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_4 + (str(csv_col_5_init + null_counter)) + csv_col_5_init_5 for null_counter in range(0,file_count_init)]
        np_col_5 = np.asarray(np_col_5)
        np_col_5 = np_col_5[np.newaxis,:]
        #for element in np_col_5: print(element)

        np_col = np.concatenate((np_col_1, np_col_2, np_col_3, np_col_4, np_col_5), axis=0)
        #for element in np_col: print(element)
        np_col = np.swapaxes(np_col, 0, 1)
        #for element in np_col: print(element)

        # Relocate directory
        p = Path(folder_path)
        p = p.parent.absolute()
        p = str(p) + "\\" + "file_list.xlsx"
        print(p)

        # Create excel file
        df = pd.DataFrame(np_col, columns=csv_col)
        try:
            df.to_excel(p, index=False)
        except PermissionError:
            print("Permission denied, please close the file and try again.")
            status = True
            pass
        if status == False: print('Execute successful, excel file exported\n')

        # Launch file explorer
        '''
        sp.Popen(f'explorer /select, "{str(p)}"')
        print('Execute successful, excel file opened')
        '''
    else:
        print('Error! Please check generate_file parameter\n\n')
        return None

    # Relocate directory
    p = Path(folder_path)
    p = str(p) + "\\"
    #print(p)
    '''# Relocate directory
    p = pl.PureWindowsPath(folder_path)
    p = str(p) + "\\"
    print(p)
    '''

    # Launch file explorer
    sp.Popen(f'explorer /select, "{str(p)}"')

    # Finish commands and store in a array
    np_col_1 = np.squeeze(np_col_1)
    np_col_2 = np.squeeze(np_col_2)
    np_col_3 = np.squeeze(np_col_3)

    for i in range(0, file_count_init):
        '''
        cmd_cm = np_col_4[i] + " \"" + np_col_1[i] + "\" \"" + np_col_3[i] + np_col_2[i] + "\""
        print(cmd_cm)
        os.system("d:;" + "cd " + p + ";" + cmd_cm) # method 1
        sp.run("d:;" + "cd " + p + ";" + cmd_cm, capture_output=True, shell=True) # method 2
        '''
        try:
            os.rename(p + np_col_1[i], p + np_col_3[i] + np_col_2[i])
        except FileExistsError:
            print("!!Possible renaming error!!\n")
            pass

    print(f'Execute successful, all {file_type} file(s) in {p} is renamed!\n')

