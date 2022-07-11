import converter_functions as cf
import PySimpleGUI as sg
import os
import webbrowser as wb

class Event_Handler_Function:
    def __init__(self, cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, hl, window, event, values):
        self.cl_single_conversion = cl_single_conversion
        self.cl_bulk_to_bulk_conversion = cl_bulk_to_bulk_conversion
        self.cl_file_merge = cl_file_merge
        self.hl = hl
        self.window = window
        self.event = event
        self.values = values
        
    def execution_log_update(self):
        print('============ Event = ', self.event, ' ==============')
        print('-------- Values Dictionary (key=value) --------')
        for key in self.values:
            print(key, ' = ',self.values[key])

    def menu_event(self):
        print("[LOG] cl_single_conversionicked " + self.event + "!")
        if self.event == self.cl_single_conversion[0]:
            sg.popup(
                "This function converts md file (table)  to csv files in the same folder. It can only convert the first table in markdown file correctly.",
                keep_on_top=True,
                title=self.cl_single_conversion[0] + ' Description'
                )
        elif self.event == self.cl_single_conversion[1]:
            sg.popup(
                "This function converts single csv file to md file (table) .",
                keep_on_top=True,
                title=self.cl_single_conversion[1] + ' Description'
                )
        elif self.event == self.cl_single_conversion[2]:
            sg.popup(
                "This function converts single xml file exported from labelimg to csv file.",
                keep_on_top=True,
                title=self.cl_single_conversion[2] + ' Description'
                )
        elif self.event == self.cl_single_conversion[3]:
            sg.popup(
                "This function converts single csv file to parquet file.",
                keep_on_top=True,
                title=self.cl_single_conversion[3] + ' Description'
                )
        elif self.event == self.cl_single_conversion[4]:
            sg.popup(
                "This function converts single parquet file to csv file.",
                keep_on_top=True,
                title=self.cl_single_conversion[4] + ' Description'
                )
        elif self.event == self.cl_single_conversion[5]:
            sg.popup(
                "This function renames the single file specified.",
                keep_on_top=True,
                title=self.cl_single_conversion[5] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[0]:
            sg.popup(
                "This function convert md files (table)  to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[0] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[1]:
            sg.popup(
                "This function convert csv files to md files (table) .",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[1] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[2]:
            sg.popup(
                "This function convert xml files to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[2] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[3]:
            sg.popup(
                "This function convert csv files to parquet files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[3] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[4]:
            sg.popup(
                "This function convert parquet files to csv files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[4] + ' Description'
                )
        elif self.event == self.cl_bulk_to_bulk_conversion[5]:
            sg.popup(
                "This function rename all the specified type of files.",
                keep_on_top=True,
                title=self.cl_bulk_to_bulk_conversion[5] + ' Description'
                )
        elif self.event == self.cl_file_merge[0]:
            sg.popup(
                "This function merges multiple csv files into one csv file.",
                keep_on_top=True,
                title=self.cl_file_merge[0] + ' Description'
                )
        elif self.event == self.cl_file_merge[1]:
            sg.popup(
                "This function merges multiple parquet files into one parquet file.",
                keep_on_top=True,
                title=self.cl_file_merge[1] + ' Description'
                )
        elif self.event == self.cl_file_merge[2]:
            sg.popup(
                "This function merges multiple md files (table) into one md file.",
                keep_on_top=True,
                title=self.cl_file_merge[2] + ' Description'
                )
        elif self.event == self.cl_file_merge[3]:
            sg.popup(
                "This function merges multiple xml files into one csv file.",
                keep_on_top=True,
                title=self.cl_file_merge[3] + ' Description'
                )
        elif self.event == self.hl[0]:
            print("[LOG] Clicked Github Repository!")
            wb.open('https://github.com/belongtothenight/File-Format-Converter')

    def listbox_update(self, listbox, folder, flag):
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fname = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
        ]
        self.window[listbox].update(fname)
        if flag == 'source':
            self.window['-R1-'].update(value=True)
            self.window['-R2-'].update(value=False)
        elif flag == 'export':
            self.window['-R1-'].update(value=False)
            self.window['-R2-'].update(value=True)
        else:
            pass
        return fname

    def conversion_source_folder(self):
        source_folder = self.values[self.event]
        print('[LOG] Source Folder = ', source_folder)
        source_folder_list = self.listbox_update("-LISTBOX-", source_folder, 'source')
        return source_folder, source_folder_list

    def conversion_source_filename(self):
        source_filename = self.values[self.event]
        print('[LOG] Source Filename = ', source_filename)
        return source_filename

    def conversion_export_folder(self):
        export_folder = self.values[self.event]
        print('[LOG] Export Folder = ', export_folder)
        export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')
        return export_folder, export_folder_list

    def conversion_export_filename(self):
        export_filename = self.values[self.event]
        print('[LOG] Export Filename = ', export_filename)
        return export_filename

    def single_conversion_filename_varification(self, converter, source_filename, export_filename, source_folder_list):
        if converter == self.cl_single_conversion[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        elif converter == self.cl_single_conversion[5]  and (source_filename in source_folder_list) :
            converter_check = 'Converter Selected: ' + converter + ' => Valid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='green')
        elif converter == self.cl_single_conversion[5] and (source_filename in source_folder_list) == False:
            converter_check = 'Source file doesn\'t exist!'
            print("[LOG] Source file doesn\'t exist!")
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        else:
            converter_check = 'Converter Selected: ' + converter + ' => InValid!'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='red')

    def single_conversion_converter(self, source_filename, export_filename, source_folder_list):
        print("[LOG] Selected Option Menu!")
        converter = self.values['-OPTION MENU-']
        print("[LOG] Converter selected: " + converter)
        converter_check = 'Converter Selected: ' + converter
        self.window['-OUTPUT-'].update(converter_check)
        try:
            self.single_conversion_filename_varification(converter, source_filename, export_filename, source_folder_list)
        except:
            converter_check = 'Please type filenames.'
            print("[LOG] " + converter_check)
            self.window['-OUTPUT-'].update(converter_check, text_color='red')
        return converter, converter_check

    def single_conversion_convert_and_export(self, converter, source_folder, export_folder, source_filename, export_filename):
        if converter == self.cl_single_conversion[0]:
            if cf.md_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[1]:
            if cf.csv_to_md(source_folder, export_folder, source_filename, export_filename, "Test", "Test") : # h1 and frame doesn't work here
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[2]:
            if cf.xml_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[3]:
            if cf.csv_to_parquet(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[4]:
            if cf.parquet_to_csv(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        elif converter == self.cl_single_conversion[5]:
            if cf.file_rename(source_folder, export_folder, source_filename, export_filename) :
                print("[LOG] Conversion complete, File exported!")
                self.window['-OUTPUT0-'].update('File exported!', text_color='green')
        else:
            print("[LOG] Conversion error, no file exported.")
            self.window['-OUTPUT0-'].update('Error!', text_color='red')
        export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')

    def single_conversion_convert_and_export_check(self, converter, converter_check, source_folder, export_folder, source_filename, export_filename):
        try:
            if converter == '':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Converter not selected.', text_color='red')
            elif converter_check == 'Please type filenames.':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[0] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[1] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[2] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[3] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[4] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Converter Selected: ' + self.cl_single_conversion[5] + ' => InValid!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
            elif converter_check == 'Source file doesn\'t exist!':
                print("[LOG] Converter selected: None")
                self.window['-OUTPUT0-'].update('Please re-type source filename.', text_color='red')
            else:
                # run conversion and export
                self.single_conversion_convert_and_export(converter, source_folder, export_folder, source_filename, export_filename)
        except:
            print("[LOG] Converter selected: None")
            self.window['-OUTPUT0-'].update('Please select converter.', text_color='red')

    def single_conversion_view_source_folder(self, source_folder):
        print("[LOG] Selected view source folder!")
        try:
            source_folder_list = self.listbox_update("-LISTBOX-", source_folder, 'source')
        except:
            source_folder = ''
            source_folder_list = self.listbox_update("-LISTBOX-", source_folder, 'source')

    def single_conversion_view_export_folder(self, export_folder):
        print("[LOG] Selected view export folder!")
        try:
            export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')
        except:
            export_folder = ''
            export_folder_list = self.listbox_update("-LISTBOX-", export_folder, 'export')

    def single_conversion_file_preview(self, source_folder, export_folder):
        if self.values['-R1-'] == True and self.values['-R2-'] == False:
            folder = source_folder
        elif self.values['-R1-'] == False and self.values['-R2-'] == True:
            folder = export_folder
        try:
            with open(folder + '/' + self.values["-LISTBOX-"][0], 'r') as f:
                self.window['-ML-'+sg.WRITE_ONLY_KEY].update('')
                source_file = f.read()
                self.window['-ML-'+sg.WRITE_ONLY_KEY].print(source_file)
                f.close()
        except:
            pass


if __name__ == '__main__':
    print("This is event handler file, not main.")