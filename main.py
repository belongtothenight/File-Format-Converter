import converter_functions as cf
import PySimpleGUI as sg

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
'''


def make_window(theme):
    sg.theme(theme)

    # Menu Layout
    menu_def = [
        ['Function List', ['Converter', ['MD to CSV', 'CSV to MD', 'XML to MD', 'CSV to Parquet', 'Parquet to CSV'], 'Rename', ['Bulk File Rename']]],
        ['Help', ['Github Repository', 'Github README.md']]
    ]
    right_click_menu_def = [[], ['Help', ['Github Repository', 'Github README.md'], 'Exit']]

    # Converter Layout
    col_1 = [
        [sg.Text('View'), sg.OptionMenu(values=('Source Folder', 'Export Folder'),  k='-OPTION MENU-')],
        [sg.Listbox(values=[], enable_events=True, size=(40, 40), key='-LISTBOX-')]
    ]

    col_2 = [
        [sg.Listbox(values=[], enable_events=True, size=(85, 42), key='-LISTBOX-')]
    ]

    converter_layout = [
        [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(key='-INPUT-')], 
        [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Export Filename (with ext) '), sg.Input(key='-INPUT-')], 
        [sg.Text('Select Converter'), sg.OptionMenu(values=('MD to CSV', 'CSV to MD', 'XML to MD', 'CSV to Parquet', 'Parquet to CSV'),  k='-OPTION MENU-'), sg.Txt(size=(17,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'), sg.Txt(size=(20,1), key='-OUTPUT-')],
        [sg.HSeparator()],
        [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
    ]

    # Rename Layout
    rename_layout = [
        [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(key='-INPUT-')], 
        [sg.Text('Export File'), sg.OptionMenu(values=('None', 'CSV', 'EXCEL'),  k='-OPTION MENU-'), sg.Text('Initial Filename Number'), sg.Input(key='-INPUT-')],
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
        sg.Tab('Converter', converter_layout),
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
        # keep an animation running so show things are happening
        
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break
        elif event == 'About':
            print("[LOG] Clicked About!")
            sg.popup('PySimpleGUI Demo All Elements',
                     'Right click anywhere to see right click menu',
                     'Visit each of the tabs to see available elements',
                     'Output of event and values can be see in Output tab',
                     'The event and values dictionary is printed after every event', keep_on_top=True)
        elif event == 'Popup':
            print("[LOG] Clicked Popup Button!")
            sg.popup("You pressed a button!", keep_on_top=True)
            print("[LOG] Dismissing Popup!")
        elif event == 'Test Progress bar':
            print("[LOG] Clicked Test Progress Bar!")
            progress_bar = window['-PROGRESS BAR-']
            for i in range(100):
                print("[LOG] Updating progress bar by 1 step ("+str(i)+")")
                progress_bar.update(current_count=i + 1)
            print("[LOG] Progress bar complete!")
        elif event == "-GRAPH-":
            graph = window['-GRAPH-']       # type: sg.Graph
            graph.draw_circle(values['-GRAPH-'], fill_color='yellow', radius=20)
            print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
        elif event == "Open Folder":
            print("[LOG] Clicked Open Folder!")
            folder_or_file = sg.popup_get_folder('Choose your folder', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose folder: " + str(folder_or_file))
        elif event == "Open File":
            print("[LOG] Clicked Open File!")
            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose file: " + str(folder_or_file))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Versions':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)

    window.close()
    exit(0)

if __name__ == '__main__':
    sg.theme('graygraygray')
    main()