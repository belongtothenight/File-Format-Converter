import converter_functions as cf
import PySimpleGUI as sg
import webbrowser as wb
import os
# prevent exe error
import sys

'''finished functions
cf.select_folder()
cf.convert_file()
cf.user_input()
cf.csv_to_md()
cf.xml_to_md()
cf.bulk_file_rename()
cf.md_to_csv(fp, mdfn, csvfn)
'''
'''
Links
    https://github.com/PySimpleGUI
    https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_All_Elements.py
    https://pysimplegui.readthedocs.io/en/latest/cookbook/#keys_1
    https://www.youtube.com/watch?v=-_z2RPAH0Qk
    https://www.youtube.com/watch?v=n6qzrBPkPqw
'''

# Variables Initialization
source_folder = ''
source_filename = ''
source_folder_list = []
export_folder = ''
export_filename = ''
export_folder_list = []
converter = ''
Converter_check = ''
final_status = ''

# Converter Function List
fl = ['MD to CSV', 'CSV to MD', 'XML to CSV', 'CSV to Parquet', 'Parquet to CSV', 'File Rename']

# Function


# PysimpleGUI Window Layout
def make_window(theme):
    sg.theme(theme)

    # Menu Layout
    menu_def = [
        ['Function List', [fl[0], fl[1], fl[2], fl[3], fl[4], fl[5]]],
        ['Help', ['Github README.md']]
    ]
    right_click_menu_def = [[], ['Help', ['Github README.md'], 'Exit']]

    # Single Convertion Layout
    col_1 = [
        [sg.Text('Files in'), sg.Radio('Source Folder', "RadioDemo", default=True, size=(10,1), k='-R1-', enable_events=True), sg.Radio('Export Folder', "RadioDemo", default=True, size=(10,1), k='-R2-', enable_events=True)],
        [sg.Listbox(values=[], enable_events=True, size=(40, 40), key='-LISTBOX-')]
    ]

    col_2 = [
        [sg.Listbox(values=[], enable_events=True, size=(85, 42), key='-LISTBOX-')]
    ]

    single_conversion_layout = [
        [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
        [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Export Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
        [sg.Text('Select Converter'), sg.OptionMenu(values=(fl[0], fl[1], fl[2], fl[3], fl[4], fl[5]),  key='-OPTION MENU-'), sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(Converter_check , size=(36,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(size=(25,1), key='-OUTPUT0-')],
        [sg.HSeparator()],
        [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
    ]

    # Bulk Convertion Layout

    # Rename Layout
    rename_layout = [
        [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(key='-INPUT-')], 
        [sg.Text('Export File'), sg.OptionMenu(values=('None', 'CSV', 'EXCEL'),  key='-OPTION MENU-'), sg.Text('Initial Filename Number'), sg.Input(key='-INPUT-')],
        [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Button('Confirm and Rename'), sg.Text('View'), sg.OptionMenu(values=('Source Folder', 'Export Folder'),  k='-OPTION MENU-')],
        [sg.HSeparator()],
        [sg.Listbox(values=[], enable_events=True, size=(135, 42), key='-LISTBOX-')]
    ]

    # Instructions Layout
    instruction_layout = [
        [sg.Text('Instructions for using this program are in this tab!')]
    ]

    # About Layout
    about_layout = [
        [sg.Text('About this program is in this tab!')]
    ]

    # Logging Layout
    logging_layout = [
        [sg.Text("Log")],
        [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
            reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
    ]

    # Layout of the whole window
    layout = [
        [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)]
    ]
    
    layout +=[[sg.TabGroup([[
        sg.Tab('Single Conversion', single_conversion_layout),
        sg.Tab('Rename', rename_layout),
        sg.Tab('Execution Log', logging_layout),
        sg.Tab('Instructions', instruction_layout),
        sg.Tab('About', about_layout)
        ]], key='-TAB GROUP-', expand_x=True, expand_y=True)
    ]]

    layout[-1].append(sg.Sizegrip())
    window = sg.Window('File Format Converter', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window

# PysimpleGUI Window Event Handler
def main():
    window = make_window(sg.theme())

    # Trigger listbox update
    def listbox_update(listbox, folder, flag):
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
        window[listbox].update(fname)
        if flag == 'source':
            window['-R1-'].update(value=True)
            window['-R2-'].update(value=False)
        elif flag == 'export':
            window['-R1-'].update(value=False)
            window['-R2-'].update(value=True)
        else:
            pass
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        # calculations


        # Event Handling
        #if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
        #    print('============ Event = ', event, ' ==============')
        #    print('-------- Values Dictionary (key=value) --------')
        #    for key in values:
        #        print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Menu Events
        elif event == fl[0]:
            print("[LOG] Clicked MD to CSV!")
            sg.popup("This function converts md files to csv files in the same folder. It can only convert the first table in markdown file correctly.", keep_on_top=True)
        elif event == fl[1]:
            print("[LOG] Clicked CSV to MD!")
            sg.popup("This function converts csv files to md files in the same folder.", keep_on_top=True)
        elif event == fl[2]:
            print("[LOG] Clicked XML to CSV!")
            sg.popup("This function converts xml files exported from labelimg to csv files.", keep_on_top=True)
        elif event == fl[3]:
            print("[LOG] Clicked CSV to Parquet!")
            sg.popup("This function converts csv files to parquet files in the same folder.", keep_on_top=True)
        elif event == fl[4]:
            print("[LOG] Clicked Parquet to CSV!")
            sg.popup("This function converts parquet files to csv files in the same folder.", keep_on_top=True)
        elif event == fl[5]:
            print("[LOG] Clicked File Rename!")
            sg.popup("This function renames the file specified.", keep_on_top=True)
        elif event == 'Github README.md':
            print("[LOG] Clicked Github Repository!")
            wb.open('https://github.com/belongtothenight/File-Format-Converter')

        # Converter Events
        elif event == '-FOLDER-':
            source_folder = values['-FOLDER-']
            print('[LOG] Folder = ', source_folder)
            # Trigger listbox update
            try:
                file_list = os.listdir(source_folder)
            except:
                file_list = []
            fname = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(source_folder, f))
                #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
            ]
            source_folder_list = file_list;
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=True)
            window['-R2-'].update(value=False)
        elif event == '-INPUT-':
            source_filename = values['-INPUT-']
            print('[LOG] Source Filename = ', source_filename)
        elif event == '-FOLDER-0':
            export_folder = values['-FOLDER-0']
            print('[LOG] Folder = ', export_folder)
            # Trigger listbox update
            try:
                file_list = os.listdir(export_folder)
            except:
                file_list = []
            fname = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(export_folder, f))
                #and f.lower().endswith(('.md', '.csv', '.xml', '.parquet')) # add file format filter
            ]
            export_folder_list = file_list;
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=False)
            window['-R2-'].update(value=True)
        elif event == '-INPUT-2':
            export_filename = values['-INPUT-2']
            print('[LOG] Export Filename = ', export_filename)
        elif event == '-CONVERTER-':
            print("[LOG] Selected Option Menu!")
            converter = values['-OPTION MENU-']
            print("[LOG] Converter selected: " + converter)
            Converter_check = 'Converter Selected: ' + converter
            window['-OUTPUT-'].update(Converter_check)
            try:
                if converter == fl[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[0] and source_filename.endswith(('.md'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                elif converter == fl[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) : # filename typed, source file exists
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[1] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.md'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                elif converter == fl[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[2] and source_filename.endswith(('.xml'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                elif converter == fl[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) : # filename typed, source file exists
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[3] and source_filename.endswith(('.csv'))  and export_filename.endswith(('.parquet'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                elif converter == fl[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) : # filename typed, source file exists
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[4] and source_filename.endswith(('.parquet'))  and export_filename.endswith(('.csv'))  and (source_filename in source_folder_list) == False: # filename typed, source file error
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                elif converter == fl[5]  and (source_filename in source_folder_list) :
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='green')
                elif converter == fl[5] and (source_filename in source_folder_list) == False:
                    Converter_check = 'Source file doesn\'t exist!'
                    print("[LOG] Source file doesn\'t exist!")
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
                else:
                    Converter_check = 'Converter Selected: ' + converter + ' => InValid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check, text_color='red')
            except:
                Converter_check = 'Please type filenames.'
                print("[LOG] " + Converter_check)
                window['-OUTPUT-'].update(Converter_check, text_color='red')
            # Export folder error check (whether folder exists)
        elif event == 'Convert and Export':
            try:
                if converter == '':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Converter not selected.', text_color='red')
                elif Converter_check == 'Please type filenames.':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[0] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[1] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[2] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[3] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[4] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Converter Selected: ' + fl[5] + ' => InValid!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please type filenames.', text_color='red')
                elif Converter_check == 'Source file doesn\'t exist!':
                    print("[LOG] Converter selected: None")
                    window['-OUTPUT0-'].update('Please re-type source filename.', text_color='red')
                else:
                    # run conversion and export
                    if converter == fl[0]:
                        if cf.md_to_csv(source_folder, export_folder, source_filename, export_filename) :
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    elif converter == fl[1]:
                        if cf.csv_to_md(source_folder, export_folder, source_filename, export_filename, "Test", "Test") : # h1 and frame doesn't work here
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    elif converter == fl[2]:
                        if cf.xml_to_csv(source_folder, export_folder, source_filename, export_filename) :
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    elif converter == fl[3]:
                        if cf.csv_to_parquet(source_folder, export_folder, source_filename, export_filename) :
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    elif converter == fl[4]:
                        if cf.parquet_to_csv(source_folder, export_folder, source_filename, export_filename) :
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    elif converter == fl[5]:
                        if cf.file_rename(source_folder, export_folder, source_filename, export_filename) :
                            print("[LOG] Conversion complete, File exported!")
                            window['-OUTPUT0-'].update('File exported!', text_color='green')
                    else:
                        print("[LOG] Conversion error, no file exported.")
                        window['-OUTPUT0-'].update('Error!', text_color='red')
                    listbox_update("-LISTBOX-", export_folder, 'export')
            except:
                print("[LOG] Converter selected: None")
                window['-OUTPUT0-'].update('Please select converter.', text_color='red')
        elif event == '-R1-':
            print("[LOG] Selected view source folder!")
            try:
                listbox_update("-LISTBOX-", source_folder, 'source')
            except:
                source_folder = ''
                listbox_update("-LISTBOX-", source_folder, 'source')
        elif event == '-R2-':
            print("[LOG] Selected view export folder!")
            try:
                listbox_update("-LISTBOX-", export_folder, 'export')
            except:
                export_folder = ''
                listbox_update("-LISTBOX-", export_folder, 'export')
        elif event == '-LISTBOX-4':
            print("[LOG] Selected Listbox!")

    window.close()
    sys.exit(0)

if __name__ == '__main__':
    sg.theme('lightgrey1')
    main()