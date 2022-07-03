import converter_functions as cf

'''finished functions
cf.select_folder()
cf.convert_file()
cf.user_input()
cf.csv_to_md()
cf.xml_to_md()
cf.bulk_rename_csv()
cf.bulk_rename_xlsx()
'''

folder_path = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/FFC/test_file/jpg/"
file_type = ".jpg"
file_name = "file_list.csv"
csv_col_3_init = 1001 #New file name starts from 1
cf.bulk_file_rename_csv(folder_path, file_type, file_name, csv_col_3_init)

# change file directory 