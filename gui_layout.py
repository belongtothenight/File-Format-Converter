import PySimpleGUI as sg

class Layout:
    def __init__(self, hl, cl_single_conversion, cl_bulk_to_bulk_conversion, cl_file_merge, Converter_check):
        self.hl = hl
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
            ['Help', [self.hl[0], self.hl[1], self.hl[2]]]
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
            [sg.Text('Click documents on the left to preview')],
            [sg.MLine(key='-ML-'+sg.WRITE_ONLY_KEY,  size=(85,42))]
        ]

        single_conversion_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse(), sg.Text('Source Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-0'), sg.FolderBrowse(), sg.Text('Export Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-0')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl_single_conversion[0], self.cl_single_conversion[1], self.cl_single_conversion[2], self.cl_single_conversion[3], self.cl_single_conversion[4], self.cl_single_conversion[5]), key='-OPTION MENU-'),
                sg.Button('Select', enable_events=True, key='-CONVERTER-'), sg.Text(self.Converter_check , size=(36,1), key='-OUTPUT-'), sg.Button('Convert and Export'), sg.Txt(key='-OUTPUT0-')],
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
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-1'), sg.FolderBrowse(), sg.Text('Source Filetype (ext)           ', text_color='gray', enable_events=True, key="-TXT-0"), sg.Input(disabled=True, enable_events=True, key='-INPUT-1')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-2'), sg.FolderBrowse(), sg.Text('New Filename Initial Number', text_color='gray', enable_events=True, key="-TXT-"), sg.Input(disabled=True, enable_events=True, key='-INPUT-2')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl_bulk_to_bulk_conversion[0], self.cl_bulk_to_bulk_conversion[1], self.cl_bulk_to_bulk_conversion[2], self.cl_bulk_to_bulk_conversion[3], self.cl_bulk_to_bulk_conversion[4], self.cl_bulk_to_bulk_conversion[5]), key='-OPTION MENU-0'),
                sg.Button('Select', enable_events=True, key='-CONVERTER-0'), sg.Text(size=(36,1), enable_events=True, key='-TXT-1'), sg.Button('Convert and Export', enable_events=True, key='-CE-'), sg.Text(enable_events=True, key='-TXT-2')],
            [sg.HSeparator()],
            [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
        ]
        return bulk_to_bulk_conversion_layout

    # File Merge Layout
    def file_merge_layout(self):
        col_1 = [
            [sg.Text('Files in'), sg.Radio('Source Folder', "RadioDemo", default=True, size=(10,1), k='-R1-3', enable_events=True), sg.Radio('Export Folder', "RadioDemo", default=True, size=(10,1), k='-R2-3', enable_events=True)],
            [sg.Listbox(values=[], enable_events=True, size=(40, 40), key='-LISTBOX-3')]
        ]

        col_2 = [
            [sg.Text('Click documents on the left to preview')],
            [sg.MLine(key='-ML-3'+sg.WRITE_ONLY_KEY,  size=(85,42))]
        ]

        file_merge_layout = [
            [sg.Text('Source Folder'), sg.In(size=(40,1), enable_events=True, key='-FOLDER-3'), sg.FolderBrowse(target='-FOLDER-3'), sg.Text('All tables in file should have the same header to prevent program failure!', text_color='red')], 
            [sg.Text('Export Folder '), sg.In(size=(40,1), enable_events=True, key='-FOLDER-4'), sg.FolderBrowse(target='-FOLDER-4'), sg.Text('Export Filename (with ext)'), sg.Input(enable_events=True, key='-INPUT-4')], 
            [sg.Text('Select Converter'), sg.OptionMenu(values=(self.cl_file_merge[0], self.cl_file_merge[1], self.cl_file_merge[2], self.cl_file_merge[3]), key='-OPTION MENU-2'),
                sg.Button('Select', enable_events=True, key='-CONVERTER-2'), sg.Text(size=(32,1), enable_events=True, key='-TXT-3'), sg.Button('Convert and Export', enable_events=True, key='-CE-2'), sg.Text(key='-TXT-4')],
            [sg.HSeparator()],
            [sg.Column(col_1,), sg.VSeparator(), sg.Column(col_2,)]
        ]
        return file_merge_layout

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
            [sg.Text('''
This tab provides a list of instructions for use of the program.

1. Single Conversion:
        This tab allows you to convert a single file from one filetype to another.
    Operation Steps:
        1. Select the source folder.
        2. Select the export folder.
        3. Select the converter.
        4. Click the select button.
        5. Select the source filename with file extension included.
        6. Select the export filename with file extension included.
        7. Click the convert and export button.
2. Bulk to Bulk Conversion:
        This tab allows you to convert all specified type of files in a folder to another.
    Operation Steps:
        1. Select the source folder.
        2. Select the export folder.
        3. Select the converter.
        4. Click the select button.
        5. For "File Rename" converter, additional source filetype and export filename initial number are required.
            Source Filetype: The filetype of the source files that you intended to rename. Example: ".xlsx", ".csv", ".txt", etc.
            Export Filename Initial Number: The initial number of the export filename. All the files are renamed with incremental number 
                based on the initial number. Example: "1", "1001", "100001", etc.
        6. Click the convert and export button.
3. File Merge:
        This tab allows you to merge multiple files into a single file.
4. Execution Log:
        This tab provides a log for every operation performed by the user, and is used to track back errors.
5. Instructions:
        Current tab.
6. About:
        This tab provides information about the program.
            ''')]
        ]
        return instruction_layout

    # About Layout
    @staticmethod
    def about_layout():
        about_layout = [
            [sg.Text('''
This program aims to provide easy and offline access to the conversion of various filetypes to other filetypes.

Developed Usage:
1. Transfer XML files generated from labelImg, which specifies the selected region coordinate of pictures and turn them into CSV files for further processing.
2. Renaming large amount of files with only a few clicks can greatly decrease the time needed when generating AI training files.
3. Able to convert between markdown, CSV, and Parquet files is extremely useful for data management since my current data is managed with Obsidian, 
    which is good for viewing data, but not for managing them.

For instructions, please refer to the instructions tab.
For more information about this project, please visit my GitHub page: https://github.com/belongtothenight/File-Format-Converter.
For issue report, please visit my GitHub Issues page to report: https://github.com/belongtothenight/File-Format-Converter/issues.
For discussion, please visit my GitHub Discussions page: https://github.com/belongtothenight/File-Format-Converter/discussions.
Mentioned links can be accessed by clicking the 'Help' element on the menu bar.
            ''')]
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
            sg.Tab('Instructions', instruction_layout),
            sg.Tab('Execution Log', execution_log_layout),
            sg.Tab('About', about_layout)
            ]], key='-TAB GROUP-', expand_x=True, expand_y=True)
        ]]
        layout[-1].append(sg.Sizegrip())
        return layout

    @staticmethod
    def window_layout(layout, right_click_menu_def):
        window = sg.Window('File Format Converter', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True, icon=r'./icon.ico')
        window.set_min_size(window.size)
        return window


if __name__ == '__main__':
    print("This is GUI layout file, not main.")