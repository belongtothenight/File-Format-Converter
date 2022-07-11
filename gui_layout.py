import PySimpleGUI as sg

class Layout:
    def __init__(self, cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, Converter_check):
        self.cl_single_conversion = cl_single_conversion
        self.cl_bulk_to_bulk_conversion = cl_bulk_to_bulk_conversion
        self.cl_file_merge = cl_file_merge
        self.Converter_check = Converter_check
    
    # Menu Layout
    def menu_layout(self):
        menu_def = [
            ['Function List',
                [
                'Single Conversion', [self.cl_single_conversion[0], self.cl_single_conversion[1], self.cl_single_conversion[2], self.cl_single_conversion[3], self.cl_single_conversion[4], self.cl_single_conversion[5]],
                'Bulk to Bulk Conversion', [self.cl_bulk_to_bulk_conversion[0], self.cl_bulk_to_bulk_conversion[1], self.cl_bulk_to_bulk_conversion[2], self.cl_bulk_to_bulk_conversion[3], self.cl_bulk_to_bulk_conversion[4], self.cl_bulk_to_bulk_conversion[5]],
                'File Merge', [self.cl_file_merge[0], self.cl_file_merge[1], self.cl_file_merge[2], self.cl_file_merge[3]]
                ]
            ],
            ['Help', ['Github README.md']]
        ]
        right_click_menu_def = [[], ['Help', ['Github README.md'], 'Exit']]
        return menu_def, right_click_menu_def

    # Single Conversion Layout
    def single_convertion_layout(self):
        col_1 = [
            [sg.Text('Files in'), sg.Radio('Source Folder', "RadioDemo", default=True, size=(10,1), k='-R1-', enable_events=True), sg.Radio('Export Folder', "RadioDemo", default=True, size=(10,1), k='-R2-', enable_events=True)],
            [sg.Listbox(values=[], enable_events=True, size=(40, 40), key='-LISTBOX-')]
        ]

        col_2 = [
            [sg.Text('Click documents on the left to preview. Support format: .txt .csv .md .xml')],
            [sg.MLine(key='-ML-'+sg.WRITE_ONLY_KEY,  size=(85,42))]
        ]

        single_conversion_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-0'), sg.FolderBrowse(), sg.Text('Export Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-0')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl_single_conversion[0], self.cl_single_conversion[1], self.cl_single_conversion[2], self.cl_single_conversion[3], self.cl_single_conversion[4], self.cl_single_conversion[5]),  key='-OPTION MENU-'), sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(self.Converter_check , size=(36,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(size=(25,1), key='-OUTPUT0-')],
            [sg.HSeparator()],
            [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
        ]
        return single_conversion_layout

    # Bulk to Bulk Conversion Layout
    def bulk_to_bulk_conversion_layout(self):
        col_1 = [
            [sg.Text('Files in Source Folder')],
            [sg.Listbox(values=[], enable_events=True, size=(62, 40), key='-LISTBOX-1')]
        ]

        col_2 = [
            [sg.Text('Files in Export Folder')],
            [sg.Listbox(values=[], enable_events=True, size=(62, 40), key='-LISTBOX-2')]
        ]

        bulk_to_bulk_conversion_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filetype (ext)           '), sg.Input(enable_events=True, key='-INPUT-')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-0'), sg.FolderBrowse(), sg.Text('New Filename Initial Number', text_color='gray'), sg.Input(disabled=True, enable_events=True, key='-INPUT-')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl_bulk_to_bulk_conversion[0], self.cl_bulk_to_bulk_conversion[1], self.cl_bulk_to_bulk_conversion[2], self.cl_bulk_to_bulk_conversion[3], self.cl_bulk_to_bulk_conversion[4], self.cl_bulk_to_bulk_conversion[5]),  key='-OPTION MENU-'), sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(self.Converter_check , size=(36,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(size=(25,1), key='-OUTPUT0-')],
            [sg.HSeparator()],
            [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
        ]
        return bulk_to_bulk_conversion_layout

    # File Merge Layout
    def file_merge_layout(self):
        file_merge_layout = [
            [sg.Text('This is File Merge', size=(40,1))],
        ]
        return file_merge_layout

    '''
    # Rename Layout
    @staticmethod
    def rename_layout():
        rename_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(key='-INPUT-')], 
            [sg.Text('Export File'), sg.OptionMenu(values=('None', 'CSV', 'EXCEL'),  key='-OPTION MENU-'), sg.Text('Initial Filename Number'), sg.Input(key='-INPUT-')],
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Button('Confirm and Rename'), sg.Text('View'), sg.OptionMenu(values=('Source Folder', 'Export Folder'),  k='-OPTION MENU-')],
            [sg.HSeparator()],
            [sg.Listbox(values=[], enable_events=True, size=(135, 42), key='-LISTBOX-1')]
        ]
        return rename_layout
    '''

    # Execution Log Layout
    @staticmethod
    def execution_log_layout():
        execution_log_layout = [
            [sg.Text("Log")],
            [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
        ]
        return execution_log_layout

    # Instructions Layout
    @staticmethod
    def instruction_layout():
        instruction_layout = [
            [sg.Text('Instructions for using this program are in this tab!')]
        ]
        return instruction_layout

    # About Layout
    @staticmethod
    def about_layout():
        about_layout = [
            [sg.Text('About this program is in this tab!')]
        ]
        return about_layout

    # Layout of the whole window
    @staticmethod
    def layout(menu_def,single_conversion_layout, bulk_to_bulk_conversion_layout, file_merge_layout,
                execution_log_layout, instruction_layout, about_layout):
        layout = [
            [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)]
        ]

        layout +=[[sg.TabGroup([[
            sg.Tab('Single Conversion', single_conversion_layout),
            sg.Tab('Bulk to Bulk Conversion', bulk_to_bulk_conversion_layout),
            sg.Tab('File Merge', file_merge_layout),
            sg.Tab('Execution Log', execution_log_layout),
            sg.Tab('Instructions', instruction_layout),
            sg.Tab('About', about_layout)
            ]], key='-TAB GROUP-', expand_x=True, expand_y=True)
        ]]
        layout[-1].append(sg.Sizegrip())
        return layout

    @staticmethod
    def window_layout(layout, right_click_menu_def):
        window = sg.Window('File Format Converter', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
        window.set_min_size(window.size)
        return window


if __name__ == '__main__':
    print("This is GUI layout file, not main.")