import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob

'''
This is the original code.
Copied from https://github.com/belongtothenight/FRCNN_Related_Code/blob/main/Format%20Converter%20xml%20to%20csv%20V2.py

path1 = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/xml'
path2 = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/train2.csv'
xml_list = []
for xml_file in glob.glob(path1 + '/*.xml'):
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
#print('data gathered')
xml_df = pd.DataFrame(xml_list, columns=column_name)
#print(xml_df, ' execute successful, dataframe data gathered')
xml_df_sort = xml_df.sort_values(by=['PicIndex'])
#print(xml_df_sort, ' execute successful, dataframe sorted')
xml_df_sort_less = xml_df_sort.drop("PicIndex", axis=1)
#print(xml_df_sort_less, ' execute successful, dataframe droped PicIndex')
xml_df_sort_less.to_csv(path2, index=False)
print(xml_df_sort_less, '\n\nexecute successful, csv file exported')
'''


def xml_to_csv(xml_file_path, csv_file_path_name):
    '''
    Description:
        This function converts xml files to csv files.
    parameter:
        Input:
            xml_file_path: path of xml files.
            csv_file_path_name: path of csv files and its file name.
        Output:
            None
    Link:
        https://github.com/belongtothenight/FRCNN_Related_Code/blob/main/Format%20Converter%20xml%20to%20csv%20V2.py
    '''
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