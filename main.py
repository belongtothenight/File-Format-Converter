import converter_functions as cf

'''select_folder_path()
cf.select_folder_path()
'''

'''select_file()
cf.select_file()
'''

'''xml_to_csv(xml_file_path, csv_file_path_name)
path1 = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/xml'
path2 = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image2/train2.csv'
cf.xml_to_csv(path1, path2)
'''

'''bulk_rename(folder_path, file_name, file_type, csv_col_3_init)
folder_path = 'D:/Note_Database/Subject/IITF Industrial Innovation and Technology Foresight/IITF Final Project/IITFFP AI Training/IITFFPAIT Rendered Image/IITFFPAITV Image1/'
file_type = ".jpg"
file_name = 'file_list.xlsx'
csv_col_3_init = 1001 #New file name starts from 1
cf.bulk_file_rename(folder_path, file_type, file_name, csv_col_3_init)
'''