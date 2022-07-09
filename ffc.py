from fnmatch import fnmatchcase
import converter_functions as cf
import PySimpleGUI as sg
import tkinter as tk
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
export_folder = ''
export_filename = ''
converter = ''
Converter_check = ''

def make_window(theme):
    sg.theme(theme)

    # Menu Layout
    menu_def = [
        ['Function List', ['Converter', ['MD to CSV', 'CSV to MD', 'XML to MD', 'CSV to Parquet', 'Parquet to CSV'], 'Rename', ['Bulk File Rename']]],
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
        [sg.Text('Select Converter'), sg.OptionMenu(values=('MD to CSV', 'CSV to MD', 'XML to MD', 'CSV to Parquet', 'Parquet to CSV'),  key='-OPTION MENU-'), sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(Converter_check , size=(35,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(size=(20,1), key='-OUTPUT-')],
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

def main():
    window = make_window(sg.theme())
    
    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        # calculations


        # Event Handling
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        # Menu Events
        elif event == 'MD to CSV':
            print("[LOG] Clicked MD to CSV!")
            sg.popup("This function converts md files to csv files in the same folder. It can only convert the first table in markdown file correctly.", keep_on_top=True)
        elif event == 'CSV to MD':
            print("[LOG] Clicked CSV to MD!")
            sg.popup("This function converts csv files to md files in the same folder.", keep_on_top=True)
        elif event == 'XML to MD':
            print("[LOG] Clicked XML to MD!")
            sg.popup("This function converts xml files exported from labelimg to csv files.", keep_on_top=True)
        elif event == 'CSV to Parquet':
            print("[LOG] Clicked CSV to Parquet!")
            sg.popup("This function converts csv files to parquet files in the same folder.", keep_on_top=True)
        elif event == 'Parquet to CSV':
            print("[LOG] Clicked Parquet to CSV!")
            sg.popup("This function converts parquet files to csv files in the same folder.", keep_on_top=True)
        elif event == 'Bulk File Rename':
            print("[LOG] Clicked Bulk File Rename!")
            sg.popup("This function renames large amount of specific type of files in a folder, and can export csv or xlsx file with cmd renaming command.", keep_on_top=True)
        elif event == 'Github README.md':
            print("[LOG] Clicked Github Repository!")
            wb.open('https://github.com/belongtothenight/File-Format-Converter')

        # Converter Events
        elif event == '-FOLDER-':
            print("[LOG] Selected Folder!")
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
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=True)
            window['-R2-'].update(value=False)
        elif event == '-INPUT-':
            print("[LOG] Typed Input!")
            source_filename = values['-INPUT-']
            print('[LOG] Source Filename = ', source_filename)
        elif event == '-FOLDER-0':
            print("[LOG] Selected Folder!")
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
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=False)
            window['-R2-'].update(value=True)
        elif event == '-INPUT-2':
            print("[LOG] Typed Input!")
            export_filename = values['-INPUT-2']
            print('[LOG] Export Filename = ', export_filename)
        elif event == '-CONVERTER-':
            print("[LOG] Selected Option Menu!")
            converter = values['-OPTION MENU-']
            print("[LOG] Converter selected: " + converter)
            Converter_check = 'Converter Selected: ' + converter
            window['-OUTPUT-'].update(Converter_check)
            try:
                if converter == 'MD to CSV' and source_filename.endswith(('.md')) == True and export_filename.endswith(('.csv')) == True:
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
                elif converter == 'CSV to MD' and source_filename.endswith(('.csv')) == True and export_filename.endswith(('.md')) == True:
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
                elif converter == 'XML to MD' and source_filename.endswith(('.xml')) == True and export_filename.endswith(('.md')) == True:
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
                elif converter == 'CSV to Parquet' and source_filename.endswith(('.csv')) == True and export_filename.endswith(('.parquet')) == True:
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
                elif converter == 'Parquet to CSV' and source_filename.endswith(('.parquet')) == True and export_filename.endswith(('.csv')) == True:
                    Converter_check = 'Converter Selected: ' + converter + ' => Valid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
                else:
                    Converter_check = 'Converter Selected: ' + converter + ' => InValid!'
                    print("[LOG] " + Converter_check)
                    window['-OUTPUT-'].update(Converter_check)
            except:
                Converter_check = 'Please type filenames.'
                print("[LOG] " + Converter_check)
                window['-OUTPUT-'].update(Converter_check)
        elif event == 'Convert and Export':
            print("[LOG] Clicked Convert and Export!")
        elif event == '-R1-':
            print("[LOG] Selected view source folder!")
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
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=True)
            window['-R2-'].update(value=False)
        elif event == '-R2-':
            print("[LOG] Selected view export folder!")
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
            window["-LISTBOX-"].update(fname)
            window['-R1-'].update(value=False)
            window['-R2-'].update(value=True)
        elif event == '-LISTBOX-4':
            print("[LOG] Selected Listbox!")

    window.close()
    sys.exit(0)

if __name__ == '__main__':
    sg.theme('lightgrey1')
    main()