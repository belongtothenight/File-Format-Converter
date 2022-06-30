import xml.etree.ElementTree as ET
import pandas as pd
import os
import glob

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